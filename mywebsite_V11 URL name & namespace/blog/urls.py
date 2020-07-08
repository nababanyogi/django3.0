from django.urls import path
from . import views
urlpatterns = [
    path('khusus/<slug:slug>/', views.khusus, name="khusus"),
    path('category/', views.categoryPost, name="category"),
    path('single/', views.singlePost, name="single"),
    path('', views.index, name="index"),
]
