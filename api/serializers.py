from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    title = serializers.CharField(required=True)
    body = serializers.CharField(required=True)
    deadline = serializers.DateTimeField(required=True)
    is_done = serializers.BooleanField(required=False)

    class Meta():
        model = Task
        fields = [
            'id', 'title', 'body', 'deadline', 'is_done'
        ]
