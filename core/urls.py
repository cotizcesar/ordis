"""wfpy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from .views import Index, UserProfileDetailView, UserUpdateView, UserProfileUpdateView, follow_view, unfollow_view, Feed, FeedPublic, Explore, ExploreUsers, PostCreateView, PostDetailView, CommentCreateView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('feed/', Feed.as_view(), name='feed'),
    path('feed/public/', FeedPublic.as_view(), name='feed_public'),
    path('explore/', Explore.as_view(), name='explore'),
    path('explore/users/', ExploreUsers.as_view(), name='explore_users'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^post/(?P<pk>\d+)/comment/$', CommentCreateView.as_view(), name='post_comment_create'),
    url(r'^u/(?P<username>[-\w]{5,30})/$', UserProfileDetailView.as_view(), name='userprofile'),
    url(r'^accounts/basic/$', UserUpdateView.as_view(), name='userprofile_basic'),
    url(r'^accounts/advanced/$', UserProfileUpdateView.as_view(), name='userprofile_advanced'),
    url(r'^u/(?P<username>[-\w]{5,30})/follow/$', follow_view, name='follow'),
    url(r'^u/(?P<username>[-\w]{5,30})/unfollow/$', unfollow_view, name='unfollow'),
]