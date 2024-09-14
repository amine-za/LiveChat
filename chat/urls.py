from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('<str:room_name>/<str:username>/', views.RoomView, name='room')
]