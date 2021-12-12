from rest_framework.response import Response

from .models import Task


def id_type_error(func):
    def wrapper(*args, **kwargs):
        try:
            int(kwargs['id'])
        except:
            return Response({"detail": "INTEGER 'id' expected"})
        return func(*args, **kwargs)
    return wrapper

def no_id_error(func):
    def wrapper(*args, **kwargs):
        try:
            Task.objects.get(id=kwargs['id'])
        except:
            return Response({"detail": "Task with this 'id' not found"})
        return func(*args, **kwargs)
    return wrapper
