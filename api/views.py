
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def allEndpoints(request):
    Endpoints = {
        "method(GET)": "mopi/all", # list all movies 
        "method(GET)": "mopi/<int:pk>", # get a single movie 
        "method(PUT)": "mopi/<int:pk>/ch",
        "method(DELETE)": "mopi/<int:pk/delete"
    }

    return Response(Endpoints)


