from rest_framework.response import Response

from .models import Task


def id_errors(func):
    def wrapper(*args, **kwargs):
        try:
            int(kwargs['id'])
        except:
            return Response({"detail": "INTEGER 'id' expected"})
        try:
            Task.objects.get(id=kwargs['id'])
        except:
            return Response({"detail": "Task with this 'id' not found"})
        return func(*args, **kwargs)
    return wrapper

def deadline_error(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime

        deadline = datetime.strptime(args[1].data['deadline'], '%Y-%m-%d %H:%M:%S')
        current_datetime = datetime.now()
        if (current_datetime>deadline):
            return Response({"detail": "Deadline should to be in the future"})
        return func(*args, **kwargs)
    return wrapper
