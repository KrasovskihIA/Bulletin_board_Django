from django.urls import path
from django.views.generic import TemplateView
from . import views
from . import views_auth



urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:post_id>/', views.PosrDetailView.as_view(), name='post_detail'),
    path('post/<int:post_id>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('post/<int:post_id>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_id>/delete_success/', TemplateView.as_view(template_name='BulletinBoard/delete_success.html'), name ='post_delete_success'),
    path('post/<int:post_id>/like/', views.PostLikeView.as_view(), name='like_post'),


    path('login/', views_auth.Login.as_view(), name='login'),
    path('logout/', views_auth.logout_views, name='logout'),
    path('', views.IndexView.as_view(), name='index'),
]