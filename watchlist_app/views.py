# from django.http.response import HttpResponse, JsonResponse
# from django.shortcuts import render
# from .models import Movie
# # Create your views here.

# def movie_list(request):
#     movies= Movie.objects.all()
#     info = movies.values()
#     data = {
#         'movies':list(info) 
#     }
#     return JsonResponse(data)


# def movie_details(request, pk):
#     movie = Movie.objects.get(pk = pk)
#     print(movie.name)
#     data = {
#         "Name":movie.name,
#         "Description":movie.description,
#         "Active":movie.active,
#     }

#     return JsonResponse(data)
