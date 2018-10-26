from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

# Django: Importing User Model
from django.contrib.auth.models import User

# Django: Generic CBV
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

# Core: Importing Models
from .models import Post

# Core: Importing forms
from .forms import PostForm

# Market: Importing Models
from market.models import Item

class Index(TemplateView):
    template_name = 'index.html'

class Feed(TemplateView):
    template_name = 'feed.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Feed, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['users'] = User.objects.all().order_by('-date_joined')[:3]
        return context

class FeedPublic(TemplateView):
    template_name = 'feed.html'

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
        return redirect('timeline_public')