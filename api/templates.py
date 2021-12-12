from .serializers import TaskSerializer
from .models import Task


class TaskViewTemplate():
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'id'
