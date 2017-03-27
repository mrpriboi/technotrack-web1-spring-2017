#from django.shortcuts import render
from blog.models import Blog, Post
from django.views.generic.base import TemplateView
from post.models import Comment
from django.views.generic.edit import FormView
from core.forms import UserRegistration
from django.shortcuts import resolve_url


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


class RegisterFormView(FormView):
    form_class = UserRegistration
    template_name = "core/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('core:login')


    #def register_user(request):
     #   if request.method == 'POST':
      #      form = UserRegistration(request.POST)
       #     if form.is_valid():
        #        form.save()
         #       return redirect('core:login')
          #  else:
           #     form = UserRegistration()

#            return render(request, 'register.html', {'form': form})#