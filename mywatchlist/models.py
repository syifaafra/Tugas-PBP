from django.db import models

# Create your models here.
class MyWatchList (models.Model) :
    title = models.CharField(max_length=255)
    watched = models.BooleanField()
    release_date = models.DateField()
    rating = models.IntegerField()
    review = models.TextField()