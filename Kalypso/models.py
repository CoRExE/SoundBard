from django.db import models


# Create your models here.
class Chat(models.Model):
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class KalypsoUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OllamaModel(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
