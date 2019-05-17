"""djangounsecure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path

from clickjacking.views import click_jacking_view
from csrf.views import CsrfView
from sqlinjection.views import sql_injection
from xss.views import xss_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clickjacking/', click_jacking_view, name='clickjacking'),
    path('csrf/', CsrfView.as_view(), name='csrf'),
    path('xss/', xss_view, name='xss'),
    path('sqlinjection/', sql_injection, name='sqlinjection'),
]
