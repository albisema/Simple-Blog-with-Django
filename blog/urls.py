from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blogForm, name='form'),
    url(r'^posts/', views.viewPosts, name='posts'),
]