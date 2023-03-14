
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("mopi/", include("api.urls")) # this will contain the endpoint urls
]
