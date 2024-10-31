"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.db import router
from django.urls import path
from django_project.category_app.views import CategoryViewSet

from rest_framework.routers import DefaultRouter

# Quado usar default router ele sabe que a raiz do projeto vir aum mapeamento das url que existe

router = DefaultRouter()
# 1º Registra a url para a API, passa uma view, e pasa um base name que é o nome da nossa view
router.register(r"api/categories", CategoryViewSet, basename="category")




urlpatterns = [
    path('admin/', admin.site.urls),

] + router.urls #fazer uma append
