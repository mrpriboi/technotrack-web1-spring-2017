from django.conf.urls import url
from .views import CommentView, CreateComment, PostCommentView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', CommentView.as_view(), name='allcomments'),
    url(r'^(?P<pk>\d+)/$', login_required(CreateComment.as_view()), name="createcomment"),
]
