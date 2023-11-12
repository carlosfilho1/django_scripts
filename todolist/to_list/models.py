from django.db import models
from django.utils import timezone

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)
    create_date = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.title
    