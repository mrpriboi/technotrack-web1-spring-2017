from django.views.generic import ListView,DetailView, CreateView, UpdateView
from blog.models import Blog, Post
from django import forms

# Create your views here.

class BlogList(ListView):
    queryset = Blog.objects.all()
    template_name = "blog/blog_list.html"

class BlogView(DetailView):
    queryset = Blog.objects.all()
    template_name = "blog/blog.html"

#class BlogForm(forms.ModelForm):
#    class Meta:
#        model = Blog
#        fields = ('caption', 'content', 'category')

class AddBlog(CreateView):
    template_name = "blog/create.html"
    model = Blog
    fields = ('caption', 'content', 'category')
    success_url = 'blog:allblogs'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddBlog,self).form_valid(form)


