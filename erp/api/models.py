from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # You can add other fields as needed

class Student(models.Model):
    created_at = models.DateTimeField()
    name = models.CharField(max_length=255)
    avatar = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    enroll_number = models.PositiveIntegerField(unique=True)

class Payment(models.Model):
    created_at = models.DateTimeField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    bill_number = models.PositiveIntegerField(unique=True)
    paid = models.PositiveIntegerField()
    balance = models.PositiveIntegerField()