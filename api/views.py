
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import status

# Create your views here.

def get_objects():
    return Movie.objects.all()


@api_view(['GET'])
def allEndpoints(request):
    Endpoints = {
        "method(GET)": "mopi/all", # list all movies 
        "method(GET)": "mopi/<int:pk>", # get a single movie 
        "method(PUT)": "mopi/<int:pk>/ch",
        "method(DELETE)": "mopi/<int:pk/delete"
    }

    return Response(Endpoints)




@api_view(['GET'])
def mopi_all(request:Request):
    movies = get_objects()
    serializer = MovieSerializer(movies, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)