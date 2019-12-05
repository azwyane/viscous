from django.urls import path,include
from . import views
import django.contrib.auth.views as auth_views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('login/',views.loginu,name='loginu'),
    path('signup/',views.signup,name='signup'),
    path('new/', views.post_new, name='post_new'),
    path('',views.welcome,name='welcome'),
    path('logout/', views.logoutu, name='logoutu'),
    path('update/', views.user_profile, name='user_profile'),
    path('edit/<int:pk>/', views.editpost, name='editpost'),
    path('delete/<int:pk>/', views.deletepost, name='deletepost'),
    path('post/<int:pk>/comment/',views.add_comment, name='add_comment'),
    path('profile/<str:username>/',views.profileclick, name='profileclick'),
    path('change-password/',auth_views.PasswordResetView.as_view(template_name='socialapp/resetpswd.html'), name='password_reset'),
    path('change-password/done/',auth_views.PasswordResetDoneView.as_view(template_name='socialapp/resetpswd_done.html'), name='password_reset_done'),
    path('change-password-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='socialapp/resetpswd_confirm.html'), name='password_reset_confirm'),
    path('change-password-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='socialapp/resetpswd_complete.html'), name='password_reset_complete'),
    path('all-people/', views.all_people, name='all_people'),
]