from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView

from .views import BlogHomeView
urlpatterns = [
	path('artikel/', include(('artikel.urls','artikel'), namespace=None)),
	path('', BlogHomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
]
