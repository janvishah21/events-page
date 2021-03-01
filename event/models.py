from django.db import models
from django.conf import settings

# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length=100)
	date = models.DateField('date')
	time = models.TimeField()
	location = models.CharField(max_length=30)
	image = models.ImageField(upload_to="event/event-img", blank=True)

	def __str__(self):
		return self.name

class Like(models.Model):
	event = models.ForeignKey(Event, related_name='likes', on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes', on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username + '-' + self.event.name

	class Meta:
		unique_together = ['event', 'user']
    