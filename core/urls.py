from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from .views import (
    Index,
    UserProfileDetailView,
    UserUpdateView,
    UserProfileUpdateView,
    follow_view,
    unfollow_view,
    Feed,
    FeedPublic,
    ExplorePosts,
    ExploreUsers,
    PostCreateView,
    PostDetailView,
    PostDeleteView,
    CommentCreateView,
)

urlpatterns = [
    path("", Index.as_view(), name="home"),
    path("feed/", Feed.as_view(), name="feed"),
    path("feed/public/", FeedPublic.as_view(), name="feed_public"),
    path("explore/posts/", ExplorePosts.as_view(), name="explore_posts"),
    path("explore/users/", ExploreUsers.as_view(), name="explore_users"),
    path("post/create/", PostCreateView.as_view(), name="post_create"),
    url(r"^post/(?P<pk>\d+)/$", PostDetailView.as_view(), name="post_detail"),
    url(r"^post/(?P<pk>\d+)/delete/$", PostDeleteView.as_view(), name="post_delete"),
    url(
        r"^post/(?P<pk>\d+)/comment/$",
        CommentCreateView.as_view(),
        name="post_comment_create",
    ),
    url(
        r"^u/(?P<username>[a-zA-Z-_\d+\.]+)/$",
        UserProfileDetailView.as_view(),
        name="userprofile",
    ),
    url(r"^accounts/basic/$", UserUpdateView.as_view(), name="userprofile_basic"),
    url(
        r"^accounts/advanced/$",
        UserProfileUpdateView.as_view(),
        name="userprofile_advanced",
    ),
    url(r"^u/(?P<username>[a-zA-Z-_\d+\.]+)/follow/$", follow_view, name="follow"),
    url(
        r"^u/(?P<username>[a-zA-Z-_\d+\.]+)/unfollow/$",
        unfollow_view,
        name="unfollow",
    ),
]
