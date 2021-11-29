from . import views
from django.urls.conf import path


urlpatterns = [
    path("list", views.MovieListAV.as_view() , name='movie-list'),
    path("list/<int:pk>", views.MovieDetailsAV.as_view(), name = 'movie-details')
]
