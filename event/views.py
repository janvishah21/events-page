from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
	events = Event.objects.all()
	return render(request, 'event/home.html', { 'events' : events })

def create(request):
	return render(request, 'event/home.html')