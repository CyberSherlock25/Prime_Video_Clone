from django.shortcuts import get_object_or_404, render

from .models import Movie


def home(request):
    movies = Movie.objects.all()
    featured_movie = movies.filter(is_featured=True).first() or movies.first()
    return render(request, "index.html", {"movies": movies, "featured_movie": featured_movie})


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, "movie_details.html", {"movie": movie})
    
