

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import Tools

urlpatterns = [
    path('tools', Tools.as_view()),
] 