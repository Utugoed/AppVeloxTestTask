from datetime import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Task
from ..serializers import TaskSerializer

# Create your tests here.
class TaskTests(APITestCase):

    def test_get_list(self):
        date_time_1 = datetime.strptime('2021-12-12 12:12:12', '%Y-%m-%d %H:%M:%S')
        task_1 = Task.objects.create(title='First task',
                                    body='This is the first task',
                                    deadline=date_time_1)
        task_2 = Task.objects.create(title='Second task',
                                    body='This is the second task',
                                    deadline=date_time_1)
        url = reverse('task_list_url')
        response = self.client.get(url)
        serializer_data = TaskSerializer([task_1, task_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, serializer_data)

    def test_get(self):
        date_time_1 = datetime.strptime('2021-12-12 12:12:12', '%Y-%m-%d %H:%M:%S')
        task_1 = Task.objects.create(title='First task',
                                    body='This is the first task',
                                    deadline=date_time_1)
        id = task_1.id
        url = reverse('task_detail_url', args=[id])
        response = self.client.get(url)
        serializer_data = TaskSerializer(task_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, serializer_data)
