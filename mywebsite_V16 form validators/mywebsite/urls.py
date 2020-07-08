from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
	path('blog/', include(('blog.urls','blog'), namespace=None)), 
	path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
