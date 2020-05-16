from django.urls import path
from .import views

urlpatterns=[
    path('login/', views.login, name='app-login'),
    path('register/', views.register, name='app-register'),
    path('logout/', views.logout, name='app-logout'),
    path('dashboard/', views.dashboard, name='app-dashboard')
]