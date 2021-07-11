from django.urls import path
from users import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth', views.auth_user, name='auth'),
    path('dashboard', views.dashboard, name='dashboard')
]
