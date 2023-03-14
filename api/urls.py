from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.allEndpoints, name="index"), 
    path("all/", views.mopi_all, name="all movies"),
    path("<int:pk>/single", views.mopi_single, name="single movie")
]
