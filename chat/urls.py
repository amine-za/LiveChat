from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('<str:contact_name>/<str:username>/', views.ChatView, name='chat')
]