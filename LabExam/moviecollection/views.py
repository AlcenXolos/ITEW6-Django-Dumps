from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, Review
from .forms import MovieForm, ReviewForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def all_movies(request):
    movies = Movie.objects.all()
    return render(request, 'moviecollection/all_movies.html', {'movies': movies})


@login_required
def home(request):
    movies = Movie.objects.filter(owner=request.user)
    return render(request, 'moviecollection/home.html', {'movies': movies, 'user': request.user})

# def movie_detail(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
#     reviews = movie.reviews.all()
#     return render(request, 'moviecollection/movie_detail.html', {'movie': movie, 'reviews': reviews})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = Review.objects.filter(movie=movie)
    can_review = request.user.is_authenticated and movie.owner == request.user
    return render(request, 'moviecollection/movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'can_review': can_review
    })


@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.owner = request.user
            movie.save()
            return redirect('home')
    else:
        form = MovieForm()
    return render(request, 'moviecollection/movie_form.html', {'form': form})

@login_required
def review_create(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.save()
            return redirect('movie_detail', pk=movie.id)
    else:
        form = ReviewForm()
    return render(request, 'moviecollection/review_form.html', {'form': form, 'movie': movie})


from django.http import HttpResponseForbidden

@login_required
def add_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if movie.owner != request.user:
        return HttpResponseForbidden("You can only review your own movies.")

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('movie_detail', movie_id=movie.id)
    else:
        form = ReviewForm()
    return render(request, 'moviecollection/review_form.html', {'form': form, 'movie': movie})
