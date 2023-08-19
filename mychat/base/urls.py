from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('room/', views.room, name='room'),

    path('get-token/', views.getToken, name='get-token'),
    path('create-member/', views.createUser, name='create-member'),
    path('get-member/', views.getMember, name='get-member'),
    path('delete-member/', views.deleteMember, name='delete-member'),
]