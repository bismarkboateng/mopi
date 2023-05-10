from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    rating = models.FloatField()
    duration = models.CharField(max_length=255)
    genre = models.CharField(max_length=255) 
    release_year = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True, blank=True, null=True)


    class Meta:
        verbose_name_plural = "Movie"

    def __str__(self):
        return f"{self.title} - {self.genre}"