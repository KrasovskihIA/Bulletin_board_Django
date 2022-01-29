from django.urls import path
from . import views



urlpatterns = [
    path('', views.IndexViews.as_view(), name='index'),
    path('create/', views.post_create, name='post_create'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
]