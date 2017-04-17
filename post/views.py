from django.shortcuts import get_object_or_404,resolve_url,HttpResponse
from django.views.generic import CreateView
from django.views.generic import DetailView, View
from .models import Post,Comment
from blog.models import Like

class CommentView(DetailView):
    queryset = Post.objects.all()
    template_name = 'post/comment.html'

class CreateComment(CreateView):

    template_name = 'post/createcomment.html'
    model = Comment
    fields = ('content',)
    post_obj = None

    def dispatch(self, request, *args, **kwargs):
        self.post_obj = get_object_or_404(Post, id=kwargs['pk'])
        return super(CreateComment, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateComment, self).get_context_data(**kwargs)
        context['post'] = self.post_obj
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.post_obj
        return super(CreateComment, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('blog:post_page', pk=self.object.post.pk)

class PostCommentView(DetailView):
    queryset = Post.objects.all()
    template_name = 'post/commentsdiv.html'
