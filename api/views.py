from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, ListAPIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.generics import  UpdateAPIView
from rest_framework.response import Response

from .utils import *


class TaskCreateAPIView(TaskViewTemplate, CreateAPIView):

    def post(self, request, *args, **kwargs):
        return self.create(is_done_deact(request), *args, **kwargs)


class TaskDestroyAPIView(TaskViewTemplate, DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TaskIsDoneAPIView(TaskViewTemplate, UpdateAPIView):

    def post(self, request, *args, **kwargs):
        return self.partial_update(is_done_act(request), *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(is_done_act(request), *args, **kwargs)


class TaskListAPIView(TaskViewTemplate, ListAPIView):
    pass


class TaskRetrieveAPIView(TaskViewTemplate, RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class TaskUpdateAPIView(TaskViewTemplate, UpdateAPIView):

    def put(self, request, *args, **kwargs):
        return self.partial_update(is_done_deact(request), *args, **kwargs)
