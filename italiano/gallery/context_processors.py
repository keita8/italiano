from .models import Gallery

def magalerie(request):
	mygallery = Gallery.objects.all()

	return dict(mygallery=mygallery)