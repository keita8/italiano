from .models import About

def about_content(request):
	restau = About.objects.all()
	return dict(restau=restau)