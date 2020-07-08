from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('sosmed/', include(('sosmed.urls','sosmed'), namespace=None)),    
    path('admin/', admin.site.urls),
]
