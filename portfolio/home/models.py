from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    number = models.CharField(max_length=11)
    textarea = models.TextField()

    def __str__(self):
        return self.name + ' - ' + self.email