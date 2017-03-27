from django.conf.urls import url
from django.contrib.auth.views import login, logout
from core.views import HomePageView
from core import views

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^login/$', login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', views.RegisterFormView.as_view() ),
]
