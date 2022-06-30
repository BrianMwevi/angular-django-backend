from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Business(models.Model):

    name = models.CharField(max_length=55)
    location = models.CharField(max_length=55)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owner')
    worth = models.PositiveIntegerField()

    def __str__(self):
        return self.name
