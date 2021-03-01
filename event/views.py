from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Like
from .forms import CreateEventForm
from django.conf import settings

# Create your views here.
def home(request, liked):
	if not request.user.is_authenticated:
		return redirect('user:signin')
	events = Event.objects.all()
	event_list = []
	for event in events:
		event_list.append({'event' : event, 'liked' : len(request.user.likes.filter(event=event)) == 0})
	print(event_list)
	return render(request, 'event/event-list.html', {'events' : event_list, 'liked' : liked})

def toggle(request, pk, liked):
	event = get_object_or_404(Event, pk=pk)
	likes = request.user.likes.filter(event=event)
	if len(likes):
		like = likes[0]
		like.delete()
	else:
		like = Like()
		like.user = request.user
		like.event = event
		like.save()

	if liked:
		return redirect('event:liked')
	else:
		return redirect('event:home')
	

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