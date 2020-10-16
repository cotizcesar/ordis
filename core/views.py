from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    FormView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils import timezone
from django.contrib import messages
from django.db.models import Count

#! Django: Importing User Model
from django.contrib.auth.models import User

#! Core: Importing Models
from .models import UserProfile, Connection, Post, Comment

#! Core: Importing forms
from .forms import UserForm, UserProfileForm, PostForm, CommentForm


class Index(TemplateView):
    template_name = "core/index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect("feed")
        return super(Index, self).get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["welcome_post"] = Post.objects.filter(featured=True).order_by(
            "-date_created"
        )[:1]
        context["users_count"] = User.objects.all().count()
        context["posts_count"] = Post.objects.all().count()
        # context['wts'] = Order.objects.filter(want='S').order_by('-date_created').exclude(is_active=False)[:5]
        # context['wtb'] = Order.objects.filter(want='B').order_by('-date_created').exclude(is_active=False)[:5]
        # context['quests'] = Quest.objects.all().order_by()
        # context['quests'] = Quest.objects.all().values('name', 'tipe','image', 'slug').order_by('quest_order')[:3]
        # context['companions'] = Item.objects.filter(tipe=2).values('name', 'image', 'slug', 'description', 'release_date').order_by('-release_date')[:3]
        # context['warframes'] = Item.objects.filter(tipe=1).values('name', 'image', 'slug', 'description', 'release_date').order_by('-release_date')[:3]
        return context


class Feed(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10
    template_name = "core/feed.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Feed, self).get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(
            Q(user__in=self.request.user.follower.values("following"))
            | Q(user=self.request.user)
        )
        return context


class FeedPublic(ListView):
    model = Post
    paginate_by = 10
    template_name = "core/feed/feed.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FeedPublic, self).get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context


class UserProfileDetailView(DetailView, FormView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    context_object_name = "profile"
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailView, self).get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(user=self.get_object())
        context["posts_count"] = Post.objects.filter(user=self.get_object()).count()

        #! Validation to show the Follow / Unfollow button.
        username = self.kwargs["username"]
        context["username"] = username
        context["user"] = self.request.user
        #! Following / Followers counters
        context["following_count"] = Connection.objects.filter(
            follower__username=username
        ).count()
        context["followers_count"] = Connection.objects.filter(
            following__username=username
        ).count()

        if username is not context["user"].username:
            result = Connection.objects.filter(
                follower__username=context["user"].username
            ).filter(following__username=username)
            context["connected"] = True if result else False
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.date_created = timezone.now()
        obj.save()
        return redirect("feed")


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "core/userprofile/userprofile_update.html"
    success_url = reverse_lazy("feed")

    def get_object(self):
        return self.request.user


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "core/userprofile/userprofile_update.html"
    success_url = reverse_lazy("feed")

    def form_valid(self, form):
        form.save(self.request.user)
        return super(UserProfileUpdateView, self).form_valid(form)

    def get_object(self):
        return self.request.user.userprofile


# Follow: hand-made system, its a better and modified copy
# https://github.com/benigls/instagram
@login_required
def follow_view(request, *args, **kwargs):
    try:
        follower = User.objects.get(username=request.user)
        following = User.objects.get(username=kwargs["username"])

    except User.DoesNotExist:
        messages.warning(
            request, "{} is not a registered user.".format(kwargs["username"])
        )
        return HttpResponseRedirect(reverse_lazy("feed"))

    if follower == following:
        messages.warning(request, "You cannot follow yourself.")

    else:
        _, created = Connection.objects.get_or_create(
            follower=follower, following=following
        )

        if created:
            messages.success(
                request, "You've successfully followed {}.".format(following.username)
            )

        else:
            messages.warning(
                request, "You've already followed {}.".format(following.username)
            )
    return HttpResponseRedirect(
        reverse_lazy("userprofile", kwargs={"username": following.username})
    )


# Unfollow: hand-made system, its a better and modified copy
# https://github.com/benigls/instagram
@login_required
def unfollow_view(request, *args, **kwargs):
    try:
        follower = User.objects.get(username=request.user)
        following = User.objects.get(username=kwargs["username"])

        if follower == following:
            messages.warning(request, "You cannot unfollow yourself.")

        else:
            unfollow = Connection.objects.get(follower=follower, following=following)
            unfollow.delete()
            messages.success(
                request, "You've just unfollowed {}.".format(following.username)
            )
    except User.DoesNotExist:
        messages.warning(
            request, "{} is not a registered user.".format(kwargs["username"])
        )
        return HttpResponseRedirect(reverse_lazy("feed"))

    except Connection.DoesNotExist:
        messages.warning(request, "You didn't follow {0}.".format(following.username))
    return HttpResponseRedirect(
        reverse_lazy("userprofile", kwargs={"username": following.username})
    )


# Connection: Followers List
class FollowersListView(LoginRequiredMixin, ListView):
    model = Connection
    template_name = "userprofile/userprofile_connection_list.html"
    context_object_name = "users"

    def get_queryset(self):
        username = self.kwargs["username"]
        return Connection.objects.all().filter(following__username=username)

    def get_context_data(self):
        context = super(FollowersListView, self).get_context_data()
        context["mode"] = "Followers"
        return context


# Connection: Following List
class FollowingListView(LoginRequiredMixin, ListView):
    model = Connection
    template_name = "userprofile/userprofile_connection_list.html"
    context_object_name = "users"

    def get_queryset(self):
        username = self.kwargs["username"]
        return Connection.objects.all().filter(follower__username=username)

    def get_context_data(self):
        context = super(FollowingListView, self).get_context_data()
        context["mode"] = "Following"
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = "post/post_create.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.date_created = timezone.now()
        obj.save()
        return redirect("feed")


class PostDetailView(DetailView):
    model = Post
    slug_field = "post_id"
    template_name = "post/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(
            post=self.object.id
        ).select_related()
        return context


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    form_class = PostForm
    template_name = "post/post_delete.html"
    success_url = reverse_lazy("feed")

    def user_passes_test(self, request):
        if request.user.is_authenticated:
            self.object = self.get_object()
            return self.object.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect("feed")
        return super(PostDeleteView, self).dispatch(request, *args, **kwargs)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    slug_field = "post_id"
    form_class = CommentForm
    template_name = "post/post_comment_create.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.post = Post.objects.get(id=self.kwargs["pk"])
        obj.user = self.request.user
        obj.save()
        return redirect("post_detail", pk=obj.post.id)


class Explore(LoginRequiredMixin, TemplateView):
    def get_context_data(self, **kwargs):
        context = super(Explore, self).get_context_data(**kwargs)
        context["users"] = (
            User.objects.all().exclude(last_login=None).order_by("-last_login")[:10]
        )
        context["posts"] = Post.objects.all().order_by("?")
        context["mode"] = "explore"
        return context


class ExploreUsers(ListView):
    model = User
    paginate_by = 1
    template_name = "core/explore.html"