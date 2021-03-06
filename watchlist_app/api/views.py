from rest_framework import viewsets
from rest_framework import mixins, serializers, status, generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .permissions import AdminOrReadOnly,ReviewUserOrReadOnly

from watchlist_app.api.serializers import ReviewSerilaizer, StreamPlatformSerializer, WatchListSerializer
from ..models import Review, StreamPlatform, WatchList
# Create your views here.


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerilaizer

    def get_queryset(self):
        return Review.objects.all()
    

    def perform_create(self, serializer):

        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)
        
        user = self.request.user
        review_query = Review.objects.filter(watchlist=movie, review_user = user )

        if(review_query.exists()):
            raise ValidationError("You have already reviewed the movie")


        if(movie.number_rating == 0):
            movie.avg_rating = serializer.validated_data['rating']

        else:
            movie.avg_rating = (serializer.validated_data['rating']+ movie.avg_rating)/2

        movie.number_rating+=1
        movie.save() 
        serializer.save(watchlist=movie, review_user = user)
        


class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerilaizer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerilaizer
    permission_classes = [ReviewUserOrReadOnly]


# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset= Review.objects.all()
#     serializer_class = ReviewSerilaizer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     # def retrieve(self, request, *args, **kwargs):
#     #     return super().retrieve(request, *args, **kwargs)
# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

#     queryset = Review.objects.all()
#     serializer_class = ReviewSerilaizer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

# class StreamPlatformListAV(APIView):
#     def get(self, request):
#         platforms = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(
#             platforms, many=True, context={'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors)


# class StreamPlatformDetailAV(APIView):
#     def get(self, request, pk):
#         try:
#             platform = StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             return Response({'Error': 'Platform not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = StreamPlatformSerializer(
#             platform, context={'request': request})
#         return Response(serializer.data)


class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(
            movies, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serilazer = WatchListSerializer(data=request.data)
        if serilazer.is_valid():
            serilazer.save()
            return Response(serilazer.data)
        else:
            return Response(serilazer.errors)


class WatchListDetailsAV(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchListSerializer.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, requests, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies= Movie.objects.all()
#         serializer = MovieSerializer(movies, many = True)
#         return Response(serializer.data)

#     if request.method =='POST':
#         serializer = MovieSerializer(data = request.data)
#         if(serializer.is_valid()):
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method =='GET':
#         try:
#             movie = Movie.objects.get(pk = pk)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie not found'}, status = status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method =='PUT':
#         movie = Movie.objects.get(pk = pk)
#         serializer = MovieSerializer(movie, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
