from django.shortcuts import render
from .models import Event
from .forms import CreateEventForm

# Create your views here.
def home(request):
	events = Event.objects.all()
	return render(request, 'event/event-list.html', { 'events' : events })

def liked(request):
	events = Event.objects.filter(is_liked=True)
	return render(request, 'event/event-list.html', { 'events' : events })

def create(request):
	create_form = CreateEventForm()
	if request.method == "POST":
		create_form = CreateEventForm(data = request.POST)
		if create_form.is_valid():
			event = Event()
			event.name = create_form.cleaned_data['name']
			event.location = create_form.cleaned_data['location']
			event.date = create_form.cleaned_data['time'].date()
			event.time = create_form.cleaned_data['time'].time()
			event.image = create_form.cleaned_data['image'].url
			event.save()

	return render(request, 'event/create-event.html', { 'create_form' : create_form })