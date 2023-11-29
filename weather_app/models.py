from djongo import models


# Create your models here.
class WeatherHistory(models.Model):
    city = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
