from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.allEndpoints, name="index"), 
    path("all/", views.mopi_all, name="all movies"),
    path("<int:pk>/single", views.mopi_single, name="single movie"), 
    path("<int:pk>/ch", views.mopi_change, name="update a movie"),
    path("new/object/", views.mopi_new, name="create a new movie")
]
