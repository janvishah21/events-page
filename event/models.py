from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('date')
    time = models.TimeField()
    location = models.CharField(max_length=30)
    image = models.ImageField(upload_to="event/event-img", blank=True)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.name