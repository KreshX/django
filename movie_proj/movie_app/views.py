from django.shortcuts import render, get_object_or_404
from .models import Movie, Actor
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
	movie = get_object_or_404(Movie, slug=slug_movie)
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