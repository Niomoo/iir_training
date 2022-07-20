from django.shortcuts import render
from django.http import HttpResponse
from movie.models import Movie
import requests

# Create your views here.

def index(request):
    return render(request, 'movie/index.html')

def get_movie_name(request, movie_name):
    return HttpResponse("Get movie name: " + movie_name)

def save_data_into_db(request, movie_name):
    all_movies = Movie.objects.all()
    for movie in all_movies:
        if movie_name == movie.movie_name:
            return HttpResponse(movie_name + " is already in database now!")
    m = Movie(movie_name = movie_name)
    m.save()
    return HttpResponse(movie_name + " is in database now!")

def get_all_data(request):
    all_movies = Movie.objects.all()
    # for movie in all_movies:
    #     print(movie.movie_name)
    return render(request, 'movie/index.html', {'movies': all_movies})

def post_movie_name(request):
    if request.method == 'POST':
        add = request.POST['movie name']
        all_movies = Movie.objects.all()
        for movie in all_movies:
            if add == movie.movie_name:
                return HttpResponse(add+ " is already in database now!")
        m = Movie(movie_name=add)
        m.save()
    return render(request, 'movie/index.html')
