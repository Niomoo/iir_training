from django.urls import path
from movie import views

urlpatterns = [
    path('home/index', views.index, name='index'),
    # path('name/<str:movie_name>/', views.get_movie_name, name='get_movie_name'),
    # path('home/save_data_into_db/<str:movie_name>/', views.save_data_into_db, name='save_data_into_db'),
    path('home/get_all_data', views.get_all_data, name='get_all_data'),
    path('home/get_all_users', views.get_all_users, name='get_all_users'),
    path('home/get_all_rating', views.get_all_rating, name='get_all_rating'),
    path('home/post_signup', views.post_signup, name='post_signup'),
    path('home/post_rating', views.post_rating, name='post_rating'),
    path('home/new_rating/<str:user_name>/', views.new_rating, name='new_rating'),
    path('home/signup', views.signup, name='signup'),
]
