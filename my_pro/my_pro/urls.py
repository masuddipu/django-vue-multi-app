"""my_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

from django.http import JsonResponse
def names(request):
    return JsonResponse({'names': ['Andaleeb', 'Dipu', 'Nasim']})

urlpatterns = [
    path('api/names/', names, name="name-api"),
    re_path(r'^home2.*$', TemplateView.as_view(template_name='index2.html'), name='end-point-2'),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html'), name='end-point'),
    path('admin/', admin.site.urls),
]
