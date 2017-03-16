from django.shortcuts import render
from django.views.generic import ListView,DetailView
from blog.models import Blog, Post

# Create your views here.

class BlogList(ListView):
    queryset = Blog.objects.all()
    template_name = "blog/blog_list.html"

class BlogView(DetailView):
    queryset = Blog.objects.all()
    template_name = "blog/blog.html"


