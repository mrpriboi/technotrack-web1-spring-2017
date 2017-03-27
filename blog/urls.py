from django.conf.urls import url
from .views import *
from post.views import CommentView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', BlogList.as_view(),name="allblogs"),
    url(r'^blog/(?P<pk>\d+)/$', BlogView.as_view(),name="oneblog"),
    url(r'^create/$', login_required(AddBlog.as_view()),name="createblog"),
    url(r'^post/(?P<pk>\d+)/$', CommentView.as_view(), name="post_page"),
]
