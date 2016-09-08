from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Movie, Theather, Time

class Home(View):
	def get(self,request):
		template_name="main/list.html"
		context={
			'movies':Movie.objects.all()
		}
		return render(request,template_name,context)

class TimeList(View):
	def get(self,request):
		template_name = 'main/horarios.html'
		horarios = Time.objects.all().order_by('schedule')
		return render(request,template_name,{'horarios':horarios})

class DetailTime(View):
	def get(self,request,id):
		template_name = 'main/detail_time.html'
		cines = Theather.objects.all().filter(theater)
		horario = Time.objects.theater(theater=cines)
		context = {
			'horario':horario,
			'cines':cines
		}
		return render(request,template_name,context)

class CineList(View):
	def get(self, request):
		template_name = 'main/cines.html'
		cines = Theather.objects.all()
		return render(request,template_name,{'cines':cines})

class DetailCine(View):
	def get(self,request,id):
		template_name = 'main/detail_cine.html'
		cine = get_object_or_404(Theather,id=id)
		movies = Movie.objects.all().filter(theater=cine)
		context = {
			'cine':cine,
			'movies':movies
		}
		return render(request,template_name,context)

class DetailMovie(View):
	def get(self,request,id):
		template_name = 'main/detail_movie.html'
		movie = get_object_or_404(Movie,id=id)
		cines = Theather.objects.all().filter(movies=movie)
		context = {
			'movie':movie,
			'cines':cines
		}
		return render(request,template_name,context)