from django.shortcuts import render, get_object_or_404
from .models import Movie, Actor, Director
from django.db.models import F, Sum, Min, Max,Count, Avg

def show_all_movie(request):
	movies = Movie.objects.order_by(F('year').desc(nulls_last=True)) #asc-по возрастанию desc-по убыванию
	for movie in movies: 
		movie.save()
	agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Max('year'))
	return render(request, 'movie_app/all_movies.html', {'movies': movies, 
		'agg':agg,
		'total': movies.count()
		})


def show_one_movie(request, slug_movie:str):
	movie = get_object_or_404(Movie, slug=slug_movie) #Передай значение в movie из таблицы Movie, где Movie.slug == slug_movie(который мы передали)
	return render(request, 'movie_app/one_movie.html', {'movie': movie})

def show_all_actor(request):
	actors = Actor.objects.all()
	# actors = get_object_or_404(Actor, slug=slug_actor)
	for actor in actors: 
		actor.save()
	return render(request, 'movie_app/all_actors.html', {'actors': actors})

def show_one_actor(request, slug_actor:str):
	actor = get_object_or_404(Actor, slug=slug_actor)
	return render(request, 'movie_app/one_actor.html', {'actor': actor})

def show_all_director(request):
	directors = Director.objects.all()
	for director in directors: 
		director.save()
	return render(request, 'movie_app/all_directors.html', {'directors': directors})

def show_one_director(request, slug_director:str):
	director = get_object_or_404(Director, slug=slug_director)
	return render(request, 'movie_app/one_director.html', {'director': director})