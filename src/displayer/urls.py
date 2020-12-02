

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import Tools, Refresher, DetailView

urlpatterns = [
    path('tools', Tools.as_view()),
    path('tools/category=<str:category>', Tools.as_view(), name='category'),
    path('tools/last_days=<str:last_days>', Tools.as_view()),
    path('tools/id=<int:id>', DetailView.as_view()),
    path('refresh', Refresher.as_view()),
] 