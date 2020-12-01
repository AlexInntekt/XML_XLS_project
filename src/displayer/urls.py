

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import Tools, Refresher

urlpatterns = [
    path('tools', Tools.as_view()),
    path('refresh', Refresher.as_view()),
] 