from django.shortcuts import render
from django.http import HttpResponse
# from .models import Gallery

# Create your views here.
def main(request):
	return render(request, 'index.html', {})


# def gallery(request):
# 	galerie = Gallery.objects.all()

# 	context = {
# 		'galerie':galerie,
# 	}

# 	return render(request, 'content/gallery.html', context)