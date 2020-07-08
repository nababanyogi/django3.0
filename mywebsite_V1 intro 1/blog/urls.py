# from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns=[
    path('recent/', views.recent),
    path('news/', views.news),
    path('', views.index),
    # url('', views.index),
]