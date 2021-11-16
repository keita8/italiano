from .models import Event

def listevent(request):
	event = Event.objects.all()

	return dict(event=event)