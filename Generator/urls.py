from django.urls import path
from appGen import views

urlpatterns = [
    path('', views.home, name='home'),
    path('password/', views.password, name='password'),
    path('aboutUs/', views.about, name='about'),
]