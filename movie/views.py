from re import M
from django.shortcuts import render, redirect
from django.http import HttpResponse
from movie.models import Movie, User, Rating
from django.db.models import Avg
import requests
import datetime

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
    movies = []
    for movie in all_movies:
        rate = Rating.objects.filter(movie_id=movie.id)
        rate_avg = rate.aggregate(Avg('rating'))['rating__avg']
        if rate_avg != None:
            rate_avg = round(rate_avg, 1)
        else:
            rate_avg = '--'
        movies.append({
            'id': movie.id,
            'movie_name': movie.movie_name, 
            'description': movie.description,
            'movie_poster': movie.movie_poster,
            'rating': rate_avg,
        })
    return render(request, 'movie/MovieList.html', {
        'movies': movies,
        'name': "Movie List",
    })

def new_movie(request):
    return render(request, 'movie/NewMovie.html', {
        'name': "New Movie",
        'years': range(1896, datetime.datetime.now().year+1)
    })

def post_movie(request):
    if request.method == 'POST':
        movie_name = request.POST['movie_name']
        description = request.POST['description']
        published_year = request.POST['published_year']
        file = request.FILES['file']
        all_movies = Movie.objects.all()
        for movie in all_movies:
            if movie_name == movie.movie_name:
                return redirect('/movie/home/get_all_data', locals())
        m = Movie(movie_name=movie_name, description=description, published_year=published_year, movie_poster=file)
        m.save()
        return redirect("/movie/home/get_all_data", locals(), {
            'movies': all_movies,
            'name': "Movie List"
        })

def get_movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'movie/MovieDetail.html', {
        'movie': movie,
        'years': range(1896, datetime.datetime.now().year+1),
        'name': "Movie Detail",
    })

def update_movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'movie/ModifyMovie.html', {
        'movie': movie,
        'years': range(1896, datetime.datetime.now().year+1),
        'name': "Modify Movie",
    })

def update_movie(request, id):
    if request.method == 'POST':
        movie_name = request.POST['movie_name']
        description = request.POST['description']
        published_year = request.POST['published_year']
        # file = request.FILES['file']
        m = Movie.objects.get(id=id)
        m.movie_name=movie_name
        m.description=description
        m.published_year=published_year
        # m.movie_poster=file
        m.save()
        all_movies = Movie.objects.all()
        return redirect("/movie/home/get_all_data", locals(), {
            'movies': all_movies,
            'name': "Movie List"
        })

def delete_movie(request, id):
    m = Movie.objects.get(id=id)
    m.delete()
    all_movies = Movie.objects.all()
    return redirect("/movie/home/get_all_data", locals(), {
        'movies': all_movies,
        'name': "Movie List"
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
            'name': "User List"
        })

def delete_user(request, user_name):
    u = User.objects.get(user_name=user_name)
    u.delete()
    all_users = User.objects.all()
    return redirect("/movie/home/get_all_users", locals(), {
        'user': all_users,
        'name': "User List"
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

def delete_rating(request, user, movie):
    user_id = User.objects.get(user_name=user).id
    movie_id = Movie.objects.get(movie_name = movie).id
    r = Rating.objects.get(user_id=user_id, movie_id=movie_id)
    r.delete()
    all_rates = Rating.objects.all()
    return redirect("/movie/home/get_all_rating", {
        'rates': all_rates,
        'name': "Rating List"
    })
