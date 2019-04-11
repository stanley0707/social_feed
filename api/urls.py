"""
URL API
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import NewsLineView

urlpatterns = [
    path("", NewsLineView.as_view()),
]