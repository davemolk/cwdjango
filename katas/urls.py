from django.urls import path
from . import views

urlpatterns = [
    path('katas/', views.katas, name='katas'),
    path('kata/<str:pk>/', views.kata, name='kata'),
    path('create-kata/', views.create_kata, name='create-kata'),
    path('update-kata/<str:pk>/', views.update_kata, name='update-kata'),
    path('delete-kata/<str:pk>/', views.delete_kata, name='delete-kata'),
    path('delete-tag/<str:pk>/', views.delete_tag, name='delete-tag'),
]
