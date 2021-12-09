from django.urls import path

from .views import TaskDestroyAPIView, TaskListAPIView, TaskListCreateAPIView
from .views import TaskRetrieveAPIView, TaskRetrieveUpdateAPIView


urlpatterns = [
    path('tasks/', TaskListAPIView.as_view(), name='tasks_url'),
    path('task/create/', TaskListCreateAPIView.as_view(),
        name='task_create_url'),
    path('task/change/<str:id>/', TaskRetrieveUpdateAPIView.as_view(),
        name='task_update_url'),
    path('task/delete/<str:id>/', TaskDestroyAPIView.as_view(),
        name='task_delete_url'),
    path('task/<str:id>/', TaskRetrieveAPIView.as_view(),
        name='task_detail_url')
]
