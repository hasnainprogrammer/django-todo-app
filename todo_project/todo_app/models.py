from django.db import models
import datetime

class Todo(models.Model):
    todo = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.todo