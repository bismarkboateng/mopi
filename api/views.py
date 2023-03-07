
# from django.http import JsonResponse

from rest_framework.response import Response
# Create your views here.
def allEndpoints(request):
    endpoints = {
        "all movies": "api/movies",
        "single movie": "api/movie/<id>"
    }

    return Response(endpoints)