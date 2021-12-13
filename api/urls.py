from django.urls import path

from .views import TaskCreateAPIView, TaskDestroyAPIView, TaskIsDoneAPIView
from .views import TaskListAPIView, TaskRetrieveAPIView, TaskUpdateAPIView


urlpatterns = [
    path('tasks/list/', TaskListAPIView.as_view(), name='task_list_url'),
    path('tasks/create/', TaskCreateAPIView.as_view(),
        name='task_create_url'),
    path('tasks/detail/<str:id>/', TaskRetrieveAPIView.as_view(),
        name='task_detail_url'),
    path('tasks/delete/<str:id>/', TaskDestroyAPIView.as_view(),
        name='task_delete_url'),
    path('tasks/is_done/<str:id>/', TaskIsDoneAPIView.as_view(),
        name='task_is_done_url'),
    path('tasks/update/<str:id>/', TaskUpdateAPIView.as_view(),
        name='task_update_url'),
]
