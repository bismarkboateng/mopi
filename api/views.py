
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import status

# Create your views here.

def get_objects(pk=None):
    if pk:
        return Movie.objects.get(pk=pk)
    return Movie.objects.all()


@api_view(['GET'])
def allEndpoints(request):
    Endpoints = {
        "method(GET)": "mopi/all", # list all movies 
        "method(GET)": "mopi/<int:pk/single>", # get a single movie 
        "method(PUT)": "mopi/<int:pk>/ch", # updating a movie
        "method(DELETE)": "mopi/<int:pk/delete"
    }

    endpoints = {
        "All Endponts": Endpoints
    }

    return Response(endpoints)



@api_view(['GET'])
def mopi_all(request:Request):
    movies = get_objects()
    serializer = MovieSerializer(movies, many=True)

    response = {
        "All Movies": serializer.data,
    }
    
    return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
def mopi_single(request:Request, pk:int):
    movie = get_objects(pk=pk)
    serializer = MovieSerializer(movie, many=False)

    response = {
        "A Single Movie": serializer.data
    }

    return Response(response, status=status.HTTP_200_OK)
