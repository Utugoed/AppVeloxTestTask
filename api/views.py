from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, ListAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.generics import  RetrieveUpdateAPIView

from .serializers import TaskSerializer, TaskUpdateSerializer
from .models import Task


class TaskDestroyAPIView(DestroyAPIView):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'id'

class TaskListAPIView(ListAPIView):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class TaskListCreateAPIView(ListCreateAPIView):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class TaskRetrieveAPIView(RetrieveAPIView):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'id'

class TaskRetrieveUpdateAPIView(RetrieveUpdateAPIView):

    serializer_class = TaskUpdateSerializer
    queryset = Task.objects.all()
    lookup_field = 'id'
