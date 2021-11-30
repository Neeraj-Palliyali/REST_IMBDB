from . import views
from django.urls.conf import path


urlpatterns = [
    path("list", views.WatchListAV.as_view() , name='movie-list'),
    path("list/<int:pk>", views.WatchListDetailsAV.as_view(), name = 'watchlist-detail'),
    path("platforms", views.StreamPlatformListAV.as_view(), name = 'stream-platform-list'),
    path("platforms/<int:pk>", views.StreamPlatformDetailAV.as_view(), name = 'streamplatform-detail'),
]
