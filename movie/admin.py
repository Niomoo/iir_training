from django.contrib import admin

# Register your models here.
from .models import Movie, User, Rating
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','movie_name')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','user_name')

admin.site.register(Movie, MovieAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Rating)