from django.views.generic import ListView,DetailView, CreateView, UpdateView
from blog.models import Blog, Post
from django import forms
from django.shortcuts import resolve_url

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

    def get_success_url(self):
        return resolve_url('blog:allblogs')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddBlog,self).form_valid(form)

class EditBlog(UpdateView):
    template_name = "blog/edit.html"
    model = Blog
    fields = ('caption', 'content', 'category')

    def get_success_url(self):
        return resolve_url('blog:oneblog', pk=self.object.pk)

    def get_queryset(self):
        return Blog.objects.filter(author = self.request.user)

class AddPost(CreateView):
    template_name = "blog/createpost.html"
    model = Post
    fields = ('content','blog')

    def get_success_url(self):
        return resolve_url('blog:post_page', pk=self.object.pk)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddPost,self).form_valid(form)

    def get_form(self, form_class = None):
        form = super(AddBlog,self).get_form()
        form.fields["blog"].queryset = Blog.objects.all().filter(author=self.request.user)



