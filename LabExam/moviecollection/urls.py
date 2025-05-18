from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.all_movies, name='all_movies'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movie/<int:movie_id>/review/', views.add_review, name='add_review'),
    # path('', views.all_movies, name='all_movies'),
    # path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/add/', views.movie_create, name='movie_create'),
    path('movie/<int:movie_id>/review/add/', views.review_create, name='review_create'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
