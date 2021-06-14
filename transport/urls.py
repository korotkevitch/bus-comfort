"""transport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from bus import views
from bus.views import IndexView, ContactView
from django.conf.urls.static import static
from django.conf import settings
from django.db import models
from django.views.generic import TemplateView

admin.site.site_header = 'Transport'  # Вместо "Администрирование Django" в админке

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('contact_view', ContactView.as_view(), name="contact_view"),
    path('thanks', TemplateView.as_view(template_name='thanks.html')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
