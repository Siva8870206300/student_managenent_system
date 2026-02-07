# api/models.py
from django.db import models   

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    token = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.email
