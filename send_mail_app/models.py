from datetime import datetime
from django.db import models
from django_celery_beat.models import CrontabSchedule
from django.contrib.auth.models import User

# Create your models here
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email =models.EmailField(max_length=100)
#     password =models.CharField(max_length=100)

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    user= models.ManyToManyField(User)
    def written_by(self):
        return",".join([str(p) for p in self.user.all()])
