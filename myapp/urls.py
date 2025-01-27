from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('update/<int:task_id>/', views.task_update, name='task_update'),
]
