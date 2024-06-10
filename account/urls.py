from . import views
from django.urls import path,re_path

app_name = 'account'

urlpatterns = [
    path('',views.index, name='index'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('change-email/',views.change_email, name='change_email'),
    path('user_detail/',views.user_detail, name='user_detail'),
    path('validate/',views.PhoneNumberValidationView.as_view(), name='validate'),
    path('user-list/',views.user_list, name='user_list'),   
    path('logout/',views.logout_user, name='logout_user'),
    path('reset_password/',views.reset_password, name='reset_password'),
    path('change_password/',views.change_password, name='change_password'),
     path('notifications/', views.NotificationListView.as_view(), name='notification-list'),
    path('notifications/<int:id>/', views.NotificationUpdateView.as_view(), name='notification-update'),
]