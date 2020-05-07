from django.shortcuts import render
from django.views.generic.base import View
from .models import Category

class ViewCategory(View):
	def get(self, request):	
		movies = Category.objects.all()
		return render(request, 'mainpage/index.html', {'index':movies})
