from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Django: Importing User Model
from django.contrib.auth.models import User

# Django: Generic CBV
from django.views.generic import TemplateView, ListView, FormView, CreateView, DetailView, UpdateView, DeleteView

# Core: Importing Models
from .models import UserProfile, Connection, Post, Comment

# Core: Importing forms
from .forms import UserForm, UserProfileForm, PostForm, CommentForm

# django-allauth: Forms
# https://django-allauth.readthedocs.io/en/latest/forms.html
#from allauth.account.forms import SignupForm

# Market: Importing Models
from market.models import Item

class Index(TemplateView):
    template_name = 'index.html'

class Feed(LoginRequiredMixin, ListView, FormView):
    model = Post
    paginate_by = 10
    template_name = 'feed/feed.html'
    form_class = PostForm

    def get_context_data(self, *args, **kwargs):
        context = super(Feed, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(Q(user__in=self.request.user.follower.values('following')) | Q(user=self.request.user))
        return context
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.date_created = timezone.now()
        obj.save()
        return redirect('home')

class FeedPublic(ListView):
    model = Post
    paginate_by = 10
    template_name = 'feed/feed.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FeedPublic, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.date_created = timezone.now()
        obj.save()
        return redirect('home')
        
class UserProfileDetailView(DetailView, FormView):
    model = User
    template_name = 'core/userprofile/userprofile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'profile'
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user=self.get_object())

        # Validation to show the Follow / Unfollow button.
        username = self.kwargs['username']
        context['username'] = username
        context['user'] = self.request.user
        # Following / Followers counters
        context['following'] = Connection.objects.filter(follower__username=username).count()
        context['followers'] = Connection.objects.filter(following__username=username).count()

        if username is not context['user'].username:
            result = Connection.objects.filter(follower__username=context['user'].username).filter(following__username=username)
            context['connected'] = True if result else False            
        return context
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.date_created = timezone.now()
        obj.save()
        return redirect('home')

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'core/userprofile/userprofile_update.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'core/userprofile/userprofile_update.html'
    success_url = reverse_lazy('home')

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
        following = User.objects.get(username=kwargs['username'])

    except User.DoesNotExist:
        messages.warning(request, '{} is not a registered user.'.format(kwargs['username']))
        return HttpResponseRedirect(reverse_lazy('home'))

    if follower == following:
        messages.warning(request, 'You cannot follow yourself.')

    else:
        _, created = Connection.objects.get_or_create(follower=follower, following=following)
        
        if (created):
            messages.success(request, 'You\'ve successfully followed {}.'.format(following.username))
        
        else:
            messages.warning(request, 'You\'ve already followed {}.'.format(following.username))
    return HttpResponseRedirect(reverse_lazy('userprofile', kwargs={'username': following.username}))

# Connection: Followers List
class FollowersListView(LoginRequiredMixin, ListView):
    model = Connection
    template_name = 'userprofile/userprofile_connection_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        username = self.kwargs['username']
        return Connection.objects.all().filter(following__username=username)

    def get_context_data(self):
        context = super(FollowersListView, self).get_context_data()
        context['mode'] = 'Followers'
        return context

# Connection: Following List
class FollowingListView(LoginRequiredMixin, ListView):
    model = Connection
    template_name = 'userprofile/userprofile_connection_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        username = self.kwargs['username']
        return Connection.objects.all().filter(follower__username=username)

    def get_context_data(self):
        context = super(FollowingListView, self).get_context_data()
        context['mode'] = 'Following'
        return context

# Unfollow: hand-made system, its a better and modified copy
# https://github.com/benigls/instagram
@login_required
def unfollow_view(request, *args, **kwargs):
    try:
        follower = User.objects.get(username=request.user)
        following = User.objects.get(username=kwargs['username'])

        if follower == following:
            messages.warning(request, 'You cannot unfollow yourself.')

        else:
            unfollow = Connection.objects.get(follower=follower, following=following)
            unfollow.delete()
            messages.success(request, 'You\'ve just unfollowed {}.'.format(following.username))
    except User.DoesNotExist:
        messages.warning(request, '{} is not a registered user.'.format(kwargs['username']))
        return HttpResponseRedirect(reverse_lazy('home'))

    except Connection.DoesNotExist:
        messages.warning(request, 'You didn\'t follow {0}.'.format(following.username))
    return HttpResponseRedirect(reverse_lazy('userprofile', kwargs={'username': following.username}))

class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'post/post_create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.date_created = timezone.now()
        obj.save()
        return redirect('home')

class PostDetailView(DetailView):
    model = Post
    slug_field = 'post_id'
    template_name = 'post/post_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object.id).select_related()
        return context

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    slug_field = 'post_id'
    form_class = CommentForm
    template_name = 'post/post_comment_create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.post = Post.objects.get(id=self.kwargs['pk'])
        obj.user = self.request.user
        obj.save()        
        return redirect('post_detail', pk=obj.post.id)

class Explore(TemplateView):
    template_name = 'explore/explore.html'

    def get_context_data(self, **kwargs):
        context = super(Explore, self).get_context_data(**kwargs)
        context['users'] = User.objects.all().order_by('?')[:10]
        context['posts'] = Post.objects.all().order_by('?')
        context['mode'] = 'explore'
        return context

class ExploreUsers(TemplateView):
    template_name = 'explore/explore.html'

    def get_context_data(self, **kwargs):
        context = super(ExploreUsers, self).get_context_data(**kwargs)
        context['users'] = User.objects.all().order_by('?')
        context['mode'] = 'explore_users'
        return context