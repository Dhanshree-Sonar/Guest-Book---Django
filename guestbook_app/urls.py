from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^sign/', views.sign, name='sign'),
]
