from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name