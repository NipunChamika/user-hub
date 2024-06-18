from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('create/', views.user_create, name='user_create'),
    path('update/<str:user_id>/', views.user_update, name='user_update'),
    path('delete/<str:user_id>/', views.user_delete, name='user_delete'),
]
