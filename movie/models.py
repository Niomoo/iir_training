from django.db import models
from unicodedata import name
import movie
import datetime

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_age = models.IntegerField()
    user_name = models.CharField(max_length=50)

year_dropdown = []
for year in range(1896, (datetime.datetime.now().year)):
    year_dropdown.append((year, year))

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    published_year = models.IntegerField(('year'), choices=year_dropdown, default=datetime.datetime.now().year+1)
    movie_poster = models.FileField(upload_to='img', blank=True)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()