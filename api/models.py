from django.db import models

# Create your models here.
class Movie(models.Model):
    
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    duration = models.CharField(max_length=255)
    genre = models.CharField(max_length=255) 
    release_year = models.DateField(null=True, blank=True)


    def __str__(self):
        return f"{self.title} - {self.genre}"