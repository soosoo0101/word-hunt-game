from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_room, name='create_room'),
    path('join/<str:room_code>/', views.join_room, name='join_room'),
    path('lobby/<str:room_code>/', views.lobby, name='lobby'),
    path('game/<str:room_code>/', views.game_view, name='game_view'),
]
