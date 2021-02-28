from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import CreateEventForm
from django.conf import settings

# Create your views here.
def home(request):
	events = Event.objects.all()
	return render(request, 'event/event-list.html', { 'events' : events, 'liked' : False })

def toggle(request, pk):
	event = get_object_or_404(Event, pk=pk)
	event.is_liked = not event.is_liked
	event.save()

	return redirect('event:home')

def liked(request):
	events = Event.objects.filter(is_liked=True)
	return render(request, 'event/event-list.html', { 'events' : events, 'liked' : True })

def upload_file(f):
    with open(settings.MEDIA_URL + 'event/event-img' + str(f._get_name()), 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def create(request):
	create_form = CreateEventForm()
	if request.method == "POST":
		create_form = CreateEventForm(request.POST)
		if create_form.is_valid():
			event = Event()
			event.name = create_form.cleaned_data['name']
			event.location = create_form.cleaned_data['location']
			event.date = create_form.cleaned_data['time'].date()
			event.time = create_form.cleaned_data['time'].time()
			# upload_file(request.FILES['image'])
			event.save()
			return redirect('event:home')

	return render(request, 'event/create-event.html', { 'create_form' : create_form })