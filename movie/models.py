from django.db import models
from unicodedata import name
import movie

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_age = models.IntegerField()
    user_name = models.CharField(max_length=50)

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    published_year = models.DateField(blank=True)
    movie_poster = models.CharField(max_length=100, blank=True)

class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()