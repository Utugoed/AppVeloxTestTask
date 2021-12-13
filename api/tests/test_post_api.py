from datetime import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Task
from ..serializers import TaskSerializer

# Create your tests here.
class TaskTests(APITestCase):

    def test_post(self):
        date_time_1 = datetime.strptime('2021-12-12 12:12:12', '%Y-%m-%d %H:%M:%S')
        url = reverse('task_create_url')
        response = self.client.post(url, {
                                            "title": "Test task",
                                            "body": "This is the test task",
                                            "deadline": date_time_1
                                            })
        expected_data = {
                        "id": 1,
                        "title": "Test task",
                        "body": "This is the test task",
                        "deadline": "2021-12-12T12:12:12Z",
                        "is_done": False
                        }
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data, expected_data)
