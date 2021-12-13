from datetime import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Task
from ..serializers import TaskSerializer

# Create your tests here.
class TaskTests(APITestCase):

    def test_delete(self):
        date_time_1 = datetime.strptime('2021-12-12 12:12:12', '%Y-%m-%d %H:%M:%S')
        task_1 = Task.objects.create(title='First task',
                                    body='This is the first task',
                                    deadline=date_time_1)
        id = task_1.id
        url = reverse('task_delete_url', args=[id])
        response = self.client.delete(url)
        expected_data = None
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(response.data, expected_data)
