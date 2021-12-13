from datetime import datetime
from django.test import TestCase

from ..models import Task
from ..serializers import TaskSerializer


class TaskSerializerTestCase(TestCase):

    def test_ok(self):
        date_time_1 = datetime.strptime('2021-12-12 12:12:12', '%Y-%m-%d %H:%M:%S')
        task_1 = Task.objects.create(title='First task',
                                    body='This is the first task',
                                    deadline=date_time_1)
        task_2 = Task.objects.create(title='Second task',
                                    body='This is the second task',
                                    deadline=date_time_1)
        data = TaskSerializer([task_1, task_2], many=True).data
        expected_data = [{
                            'id': 1,
                            'title': 'First task',
                            'body': 'This is the first task',
                            'deadline': '2021-12-12T12:12:12Z',
                            'is_done': False
                        },
                        {
                            'id': 2,
                            'title': 'Second task',
                            'body': 'This is the second task',
                            'deadline': '2021-12-12T12:12:12Z',
                            'is_done': False
                        }]
        self.assertEqual(expected_data, data)
