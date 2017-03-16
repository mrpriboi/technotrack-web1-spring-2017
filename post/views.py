from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post

class CommentView(DetailView):
    queryset = Post.objects.all()
    template_name = 'post/comment.html'