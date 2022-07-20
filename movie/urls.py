from django.urls import path
from movie import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('name/<str:movie_name>/', views.get_movie_name, name='get_movie_name'),
    path('home/save_data_into_db/<str:movie_name>/', views.save_data_into_db, name='save_data_into_db'),
    path('home/get_all_data', views.get_all_data, name='get_all_data'),
]
