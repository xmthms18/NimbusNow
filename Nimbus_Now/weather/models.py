from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class SavedWeatherData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=200)
    icon = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username} - {self.city}"