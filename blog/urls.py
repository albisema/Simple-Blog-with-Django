from django.conf.urls import url
from .views import blogForm

urlpatterns = [
    url(r'^$', blogForm, name='form'),
]