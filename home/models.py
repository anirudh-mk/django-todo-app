import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    status = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class UserTodoLink(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4())
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
