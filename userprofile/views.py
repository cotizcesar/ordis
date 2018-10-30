from django.shortcuts import render

# Django: Importing User Model
from django.contrib.auth.models import User

# Django: Generic CBV
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

# Post: Importing Models
from core.models import Connection, Post

class UserProfileDetailView(DetailView):
    model = User
    template_name = 'userprofile_index.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'profile'

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