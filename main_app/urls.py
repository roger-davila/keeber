from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('keyboards/', views.keyboards_index, name='index'),
  path('accounts/signup/', views.signup, name='signup'),
]
