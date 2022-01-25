from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexViews.as_view(), name='index'),
]