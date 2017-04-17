# coding: utf-8
from django.db.models import Q
from django.views.generic import ListView,DetailView, CreateView, UpdateView
from blog.models import Blog, Post, Like
from django import forms
from django.shortcuts import resolve_url,get_object_or_404, HttpResponse

# Create your views here.

class BlogList(ListView):
    queryset = Blog.objects.all()
    template_name = "blog/blog_list.html"
    sortform = None

    def dispatch(self, request, *args, **kwargs):
        self.sortform = SortForm(self.request.GET)
        return super(BlogList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['sortform'] = self.sortform
        return context

    def get_queryset(self):
        qs = super(BlogList, self).get_queryset()
        if self.sortform.is_valid():
            value = self.sortform.cleaned_data.get('sort')
            if value:
                qs = qs.order_by(value)

            value = self.sortform.cleaned_data.get('search')
            if value:
                qs = qs.filter(
                    Q(caption__icontains=value)
                    | Q(content__icontains=value)
                )
        return qs


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
    fields = ('title','content','blog')

    def get_success_url(self):
        return resolve_url('blog:post_page', pk=self.object.pk)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddPost,self).form_valid(form)

    def get_form(self, form_class=None):
        form = super(AddPost,self).get_form()
        form.fields["blog"].queryset = Blog.objects.all().filter(author=self.request.user)
        return form

class CreatePost(CreateView):
    template_name = "blog/addpost.html"
    model = Post
    fields = ('title','content','blog')

    def get_success_url(self):
        return resolve_url('blog:post_page', pk=self.object.pk)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost,self).form_valid(form)

    def get_form(self, form_class=None):
        form = super(CreatePost,self).get_form()
        form.fields["blog"].queryset = Blog.objects.all().filter(author=self.request.user)
        return form

class EditPost(UpdateView):

    template_name = 'blog/editpost.html'
    model = Post
    fields = ('title','content',)

    def get_queryset(self):
        return super(EditPost, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return resolve_url('blog:post_page', pk=self.object.pk)


class SortForm(forms.Form):

    sort = forms.ChoiceField(choices={
        ('caption', u'Заголовок'),
        ('created_at', u'Дата создания'),
    },
        required=False, widget=forms.RadioSelect
    )
    search = forms.CharField(required=False, widget=forms.TextInput)

class AddPostFromBlog(CreateView):
    template_name = "blog/createpostfromblog.html"
    model = Post
    fields = ('title','content',)
    blog = None

    def dispatch(self, request, *args, **kwargs):
        self.blog = get_object_or_404(Blog, id=kwargs['pk'])
        return super(AddPostFromBlog, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return resolve_url('blog:post_page', pk=self.object.pk)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = self.blog
        return super(AddPostFromBlog, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AddPostFromBlog, self).get_context_data(**kwargs)
        context['blog'] = self.blog
        return context

def likepost(request, pk=None):
    post = get_object_or_404(Post, id=pk)
    if request.user.is_authenticated:
        like = Like.objects.filter(post=post, author=request.user).first()
        if not like:
            like = Like(post=post, author=request.user)
            like.save()
        else:
            like.delete()
    return HttpResponse(Like.objects.filter(post=post).count())

def countlikes(request, pk=None):
    post = get_object_or_404(Post, id=pk)
    return HttpResponse(Like.objects.filter(post=post).count())