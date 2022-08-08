from django.shortcuts import render, redirect
from django.http import HttpResponse
from movie.models import Movie, User, Rating
import requests

# Create your views here.

def index(request):
    all_movies = Movie.objects.all()
    return render(request, 'movie/index.html', {
        'movies': all_movies,
        'name': "Movie Ranking",
    })

# def get_movie_name(request, movie_name):
#     return HttpResponse("Get movie name: " + movie_name)

# def save_data_into_db(request, movie_name):
#     all_movies = Movie.objects.all()
#     for movie in all_movies:
#         if movie_name == movie.movie_name:
#             return HttpResponse(movie_name + " is already in database now!")
#     m = Movie(movie_name = movie_name)
#     m.save()
#     return HttpResponse(movie_name + " is in database now!")

def get_all_data(request):
    all_movies = Movie.objects.all()
    return render(request, 'movie/MovieList.html', {
        'movies': all_movies,
        'name': "Movie List",
    })

def new_movie(request):
    return render(request, 'movie/MovieList.html', {
        'movies': all_movies,
        'name': "Movie List",
    })

# def post_movie_name(request):
#     if request.method == 'POST':
#         add = request.POST['movie name']
#         all_movies = Movie.objects.all()
#         for movie in all_movies:
#             if add == movie.movie_name:
#                 return HttpResponse(add+ " is already in database now!")
#         m = Movie(movie_name=add)
#         m.save()
#     return render(request, 'movie/index.html')

def get_all_users(request):
    all_users = User.objects.all()
    return render(request, 'movie/UserList.html', {
        'users': all_users,
        'name': "User List",
    })

def signup(request):
    return render(request, 'movie/NewUser.html', {
        'name': "New User"
    })

def post_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        age = request.POST['age']
        all_users = User.objects.all()
        for user in all_users:
            if username == user.user_name:
                return redirect('/movie/home/signup', locals())
        u = User(user_name=username, user_age=age)
        u.save()
        return redirect("/movie/home/get_all_users", locals(), {
            'name': "User"
        })

def get_all_rating(request):
    all_rates = Rating.objects.all()
    rates = []
    for rate in all_rates:
        rating = rate.rating
        movie = Movie.objects.get(id=rate.movie.id).movie_name
        user = User.objects.get(id=rate.user.id).user_name
        rates.append({'movie': movie, 'user': user, 'rating': rating})
    return render(request, 'movie/RatingList.html', {
        'rates': rates,
        'name': "Rating List",
    })

def new_rating(request, user_name):
    all_movies = Movie.objects.all()
    all_users = User.objects.all()
    return render(request, 'movie/NewRating.html', {
        'movies': all_movies,
        'users': all_users,
        'name': "New Rating",
        'user_name': user_name,
    })

def post_rating(request):
    if request.method == 'POST':
        username = request.POST['username']
        movie_id = request.POST['movie']
        rating = request.POST['rating']
        print(username, movie_id, rating)
        user = User.objects.get(user_name=username)
        movie = Movie.objects.get(id=movie_id)
        r = Rating(user=user, movie=movie, rating=rating)
        r.save()
        all_rates = Rating.objects.all()
        return redirect("/movie/home/get_all_rating", {
            'rates': all_rates,
            'name': "Rating List"
        })

