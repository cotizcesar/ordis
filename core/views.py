from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

# Django: Importing User Model
from django.contrib.auth.models import User

# Django: Generic CBV
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

# Core: Importing Models
from .models import Post, Comment

# Core: Importing forms
from .forms import PostForm

# Market: Importing Models
from market.models import Item

class Index(TemplateView):
    template_name = 'index.html'

class Feed(LoginRequiredMixin, TemplateView):
    template_name = 'feed/feed.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Feed, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['users'] = User.objects.all().order_by('-date_joined')[:3]
        return context

class FeedPublic(TemplateView):
    template_name = 'feed/feed.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FeedPublic, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['users'] = User.objects.all().order_by('-date_joined')[:3]
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'post/post_create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.date_created = timezone.now()
        obj.save()
        return redirect('feed')

class PostDetailView(DetailView):
    model = Post
    slug_field = 'post_id'
    template_name = 'post/post_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object.id).select_related()
        return context

class ExploreUsers(TemplateView):
    template_name = 'explore/explore_users.html'

    def get_context_data(self, **kwargs):
        context = super(ExploreUsers, self).get_context_data(**kwargs)
        context['users'] = User.objects.all().order_by('?')
        #context['mode'] = 'explore_users'
        return context