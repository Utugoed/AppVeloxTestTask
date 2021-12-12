from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, ListAPIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.generics import  UpdateAPIView
from rest_framework.response import Response

from .exceptions import *
from .templates import TaskViewTemplate
from .utils import *


class TaskCreateAPIView(TaskViewTemplate, CreateAPIView):

    def post(self, request, *args, **kwargs):
        return self.create(is_done_deact(request), *args, **kwargs)


class TaskDestroyAPIView(TaskViewTemplate, DestroyAPIView):

    @id_type_error
    @no_id_error
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TaskIsDoneAPIView(TaskViewTemplate, UpdateAPIView):

    @id_type_error
    @no_id_error
    def patch(self, request, *args, **kwargs):
        return self.partial_update(is_done_act(request), *args, **kwargs)

    @id_type_error
    @no_id_error
    def put(self, request, *args, **kwargs):
        return self.partial_update(is_done_act(request), *args, **kwargs)


class TaskListAPIView(TaskViewTemplate, ListAPIView):
    pass


class TaskRetrieveAPIView(TaskViewTemplate, RetrieveAPIView):

    @id_type_error
    @no_id_error
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class TaskUpdateAPIView(TaskViewTemplate, UpdateAPIView):

    @id_type_error
    @no_id_error
    def patch(self, request, *args, **kwargs):
        return self.partial_update(is_done_deact(request), *args, **kwargs)

    @id_type_error
    @no_id_error
    def put(self, request, *args, **kwargs):
        return self.partial_update(is_done_deact(request), *args, **kwargs)
