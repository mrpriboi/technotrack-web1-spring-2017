from django.conf.urls import url,include
from .views import *
from post.views import CommentView

urlpatterns = [
    url(r'^$', BlogList.as_view(),name="allblogs"),
    url(r'^blog/(?P<pk>\d+)/$', BlogView.as_view(),name="oneblog"),
    url(r'^post/(?P<pk>\d+)/$', CommentView.as_view(), name="post_page"),
]
