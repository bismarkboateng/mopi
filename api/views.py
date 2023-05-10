
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
        "method(GET)": "mopi/movies/<int:pk>", # get a single movie 
        "method(PUT)": "mopi/<int:pk>/ch", # updating a movie
        "method(DELETE)": "mopi/<int:pk/delete",
        "method(POST)": "mopi/new/object" # create a new post object
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



@api_view(['PUT'])
def mopi_change(request:Request, pk:int):
    movie = get_objects(pk=pk)
    data = request.data 
    serializer = MovieSerializer(instance=movie, data=data)

    if serializer.is_valid():
        serializer.save()

        response = {
            "message": "Post Updated Succesfully!",
            "data": serializer.data
        }

        return Response(response, status=status.HTTP_200_OK)
    

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def mopi_new(request: Request):
    data = request.data 
    serializer = MovieSerializer(data=data)

    if serializer.is_valid():
        serializer.save()

        response = {
            "message":"Post Created Successfully!",
            "data": serializer.data
        }

        return Response(response, status=status.HTTP_201_CREATED)
    

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def mopi_delete(request:Request, pk:int):
    movie = get_objects(pk=pk)
    movie.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
