from datetime import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Task
from ..serializers import TaskSerializer

# Create your tests here.
class TaskTests(APITestCase):

    def test_put_update(self):
        date_time_1 = datetime.strptime('2021-12-12 12:12:12', '%Y-%m-%d %H:%M:%S')
        date_time_2 = datetime.strptime('2021-12-13 13:13:13', '%Y-%m-%d %H:%M:%S')
        task_1 = Task.objects.create(title='First task',
                                    body='This is the first task',
                                    deadline=date_time_1)
        id = task_1.id
        url = reverse('task_update_url', args=[id])
        response = self.client.put(url, {
                                        "title": "Test task",
                                        "deadline": date_time_2,
                                        "is_done": True
                                        })
        expected_data = {
                        "id": 1,
                        "title": "Test task",
                        "body": "This is the first task",
                        "deadline": "2021-12-13T13:13:13Z",
                        "is_done": False
                        }
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)


    def test_patch_update(self):
        date_time_1 = datetime.strptime('2021-12-12 12:12:12', '%Y-%m-%d %H:%M:%S')
        date_time_2 = datetime.strptime('2021-12-13 13:13:13', '%Y-%m-%d %H:%M:%S')
        task_1 = Task.objects.create(title='First task',
                                    body='This is the first task',
                                    deadline=date_time_1)
        id = task_1.id
        url = reverse('task_update_url', args=[id])
        response = self.client.patch(url, {
                                        "title": "Test task",
                                        "body": "This is the test task",
                                        "deadline": date_time_2,
                                        "is_done": True
                                        })
        expected_data = {
                        "id": 1,
                        "title": "Test task",
                        "body": "This is the test task",
                        "deadline": "2021-12-13T13:13:13Z",
                        "is_done": False
                        }
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)


    def test_put_is_done(self):
        date_time_1 = datetime.strptime('2021-12-12 12:12:12', '%Y-%m-%d %H:%M:%S')
        date_time_2 = datetime.strptime('2021-12-13 13:13:13', '%Y-%m-%d %H:%M:%S')
        task_1 = Task.objects.create(title='First task',
                                    body='This is the first task',
                                    deadline=date_time_1)
        id = task_1.id
        url = reverse('task_is_done_url', args=[id])
        response = self.client.put(url, {
                                        "title": "Test task",
                                        "body": "This is the test task",
                                        "deadline": date_time_2,
                                        "is_done": False
                                        })
        expected_data = {
                        "id": 1,
                        "title": "First task",
                        "body": "This is the first task",
                        "deadline": "2021-12-12T12:12:12Z",
                        "is_done": True
                        }
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)


    def test_patch_is_done(self):
        date_time_1 = datetime.strptime('2021-12-12 12:12:12', '%Y-%m-%d %H:%M:%S')
        date_time_2 = datetime.strptime('2021-12-13 13:13:13', '%Y-%m-%d %H:%M:%S')
        task_1 = Task.objects.create(title='First task',
                                    body='This is the first task',
                                    deadline=date_time_1)
        id = task_1.id
        url = reverse('task_is_done_url', args=[id])
        response = self.client.patch(url, {
                                        "title": "Test task",
                                        "body": "This is the test task",
                                        "deadline": date_time_2,
                                        "is_done": True
                                        })
        expected_data = {
                        "id": 1,
                        "title": "First task",
                        "body": "This is the first task",
                        "deadline": "2021-12-12T12:12:12Z",
                        "is_done": True
                        }
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data, expected_data)
