from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

