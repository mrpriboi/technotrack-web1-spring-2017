from django.shortcuts import render
from blog.models import Blog, Post
from django.views.generic.base import TemplateView
from post.models import Comment

# Create your views here.

class HomePageView(TemplateView):
    queryset = Blog.objects.all()
    queryset = Post.objects.all()
    queryset = Comment.objects.all()
    template_name = "core/main.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['blogs_count'] = Blog.objects.all().count()
        context['posts_count'] = Post.objects.all().count()
        context['comment_count'] = Comment.objects.all().count()
        return context
