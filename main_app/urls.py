from django.urls import path
from django.contrib.auth.views import LoginView
from main_app.forms import UserLoginForm
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('keyboards/', views.keyboards_index, name='index'),
  path('accounts/signup/', views.signup, name='signup'),
  path(
    'accounts/login/', 
    LoginView.as_view(authentication_form = UserLoginForm),
    name="login"
  ),
  path('user/<int:user_id>/', views.user_profile, name='profile'),
  path('user/<int:user_id>/keyboards/', views.user_keyboards, name='keyboards'),
]
