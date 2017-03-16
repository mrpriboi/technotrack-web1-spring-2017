from blog.views import BlogList, BlogView
from django.conf.urls import url
from .views import CommentView

urlpatterns = [
    url(r'^$', CommentView.as_view(), name='allcomments'),
]
