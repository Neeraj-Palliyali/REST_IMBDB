from . import views
from rest_framework.routers import DefaultRouter
from django.urls.conf import path  , include

router = DefaultRouter()
router.register('platform', views.StreamPlatformVS, basename = 'streamplatform' )

urlpatterns = [
    path("list", views.WatchListAV.as_view(), name='movie-list'),
    path("list/<int:pk>", views.WatchListDetailsAV.as_view(),
         name='watchlist-detail'),
    
    
    path('', include(router.urls)),
    # path("platforms", views.StreamPlatformListAV.as_view(),
    #      name='stream-platform-list'),
    # path("platforms/<int:pk>", views.StreamPlatformDetailAV.as_view(),
    #      name='streamplatform-detail'),

    # path("reviews", views.ReviewList.as_view(), name="review-list"),
    # path("reviews/<int:pk>", views.ReviewDetail.as_view(), name="review-detail"),
    path("platforms/<int:pk>/review-create",
         views.ReviewCreate.as_view(), name="review-create"),
    path("platforms/<int:pk>/reviews",
         views.ReviewList.as_view(), name="review-list"),
    path("platforms/reviews/<int:pk>",
         views.ReviewDetail.as_view(), name="review-detail"),

]
