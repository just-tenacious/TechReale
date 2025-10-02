from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=150, unique=True)
    email=models.EmailField(unique=True)

    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.username   


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username
    