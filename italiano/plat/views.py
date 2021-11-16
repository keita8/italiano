from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Plat
# Create your views here.

# def dishelist(request):
# 	dishe = Plat.objects.all()

# 	context = {'dishe':dishe}

# 	return render(request, 'content/dishes.html', context)
 