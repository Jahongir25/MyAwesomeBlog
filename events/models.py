from django.db import models
class Event(models.Model):
    event_Image=models.ImageField(upload_to="event_images/")
    event_Text=models.CharField(max_length=300)


# Create your models here.
