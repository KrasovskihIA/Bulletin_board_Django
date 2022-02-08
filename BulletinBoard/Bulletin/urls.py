from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from . import views
from . import views_auth
from django.urls.base import reverse_lazy
from .views import CategorySearch



urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:post_id>/', views.PosrDetailView.as_view(), name='post_detail'),
    path('post/<int:post_id>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('post/<int:post_id>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_id>/delete_success/', TemplateView.as_view(template_name='BulletinBoard/delete_success.html'), name ='post_delete_success'),
    path('post/<int:post_id>/like/', views.PostLikeView.as_view(), name='like_post'),
    path('search/', CategorySearch.as_view(), name='search_results'),

    path('<int:user_id>/profile/', views_auth.ProfileView.as_view(), name ='profile'),
    path('<int:user_id>/profile/update/', views_auth.UpdateProfileView.as_view(), name ='update_profile'),

    path('signup/', views_auth.SignupViews.as_view(), name='signup'),
    path('login/', views_auth.Login.as_view(), name='login'),
    path('logout/', views_auth.logout_views, name='logout'),

    path('password_resset/', PasswordResetView.as_view(
        success_url=reverse_lazy('password_resset_done'),
        template_name = 'my_auth/password_reset.html',
        email_template_name = 'my_auth/password_reset_email.html'),
        name='password_resset'),
    path('password_resset/done/', PasswordResetDoneView.as_view(
        template_name='my_auth/password_reset_done.html'),
        name='password_resset_done'),
    path('password_resset/<str:uidb64>/<slug:token>/', PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('password_reset_complete'),
        template_name='my_auth/password_reset_confirm.html'),
        name='password_reset_confirm'),

    path('password_reset/complete/', PasswordResetCompleteView.as_view(
        template_name='my_auth/password_reset_complete.html'),
        name='password_reset_complete'),

    path('', views.IndexView.as_view(), name='index'),
]