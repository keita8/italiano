from .models import Plat

def listplat(request):
	
	obj = Plat.objects.all()
	return dict(obj=obj)