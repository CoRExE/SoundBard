from django.db import models


# Create your models here.
class Sound(models.Model):
    title = models.CharField(max_length=100)
    sound = models.FileField(upload_to='static/SoundBard/sounds/', null=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name
