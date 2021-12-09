from django.db import models


class Task(models.Model):

    title = models.CharField(max_length=150)
    body = models.CharField(max_length=1500)
    deadline = models.DateTimeField()
    is_done = models.BooleanField(default='False')

    def __str__(self):
        return self.title
