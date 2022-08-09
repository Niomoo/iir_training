from django.urls import path
from movie import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/index', views.index, name='index'),
    # path('name/<str:movie_name>/', views.get_movie_name, name='get_movie_name'),
    # path('home/save_data_into_db/<str:movie_name>/', views.save_data_into_db, name='save_data_into_db'),
    path('home/get_all_data', views.get_all_data, name='get_all_data'),
    path('home/get_all_users', views.get_all_users, name='get_all_users'),
    path('home/get_all_rating', views.get_all_rating, name='get_all_rating'),
    path('home/post_movie', views.post_movie, name='post_movie'),
    path('home/post_signup', views.post_signup, name='post_signup'),
    path('home/post_rating', views.post_rating, name='post_rating'),
    path('home/new_movie', views.new_movie, name='new_movie'),
    path('home/signup', views.signup, name='signup'),
    path('home/new_rating/<str:user_name>/', views.new_rating, name='new_rating'),
    path('home/get_movie_detail/<int:id>/', views.get_movie_detail, name='get_movie_detail'),
    path('home/update_movie_detail/<int:id>/', views.update_movie_detail, name='update_movie_detail'),
    path('home/update_movie/<int:id>/', views.update_movie, name='update_movie'),
    path('home/delete_movie/<int:id>/', views.delete_movie, name='delete_movie'),
    path('home/delete_user/<str:user_name>/', views.delete_user, name='delete_user'),
    path('home/delete_rating/<str:user>/<str:movie>', views.delete_rating, name='delete_rating'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
