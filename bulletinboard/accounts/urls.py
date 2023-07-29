from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
  path('home/', views.home, name='home'),
  path('registration/', views.registration, name='registration'),
  path('active_user/<uuid:token>/', views.active_user, name='active_user'),
  path('login_page/', views.login_page, name='login_page'), 
  path('logout_page/', views.logout_page, name='logout_page'),
  path('edit_page/', views.edit_page, name='edit_page'), 
  path('change_password/', views.change_password,name='change_password'),
]

import django.conf.urls as url
from accounts import views
url.handler500 = 'accounts.views.my_error_handler' 