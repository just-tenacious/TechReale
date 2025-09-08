from django.urls import path
from home import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/',views.register_view,name='register'),
     path('verify-email/', views.verify_email_view, name='verify_email'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.user_list, name='user_list'),
    path('users/add/', views.add_user, name='add_user'),
    path('users/update/<int:user_id>/', views.update_user, name='update_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
]
