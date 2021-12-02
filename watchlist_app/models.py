from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class StreamPlatform (models.Model):
    name =models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField( max_length=200)

    def __str__(self) -> str:
        return self.name
class WatchList(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField( max_length=200)
    patform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name= "watchlist", null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField( auto_now_add=True)

    def __str__(self) :
        return self.name

class Review(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField( max_length=200, null= True )
    watchlist = models.ForeignKey(WatchList,on_delete=models.CASCADE, related_name="reviews")
    active = models.BooleanField(default= True)
    created = models.DateTimeField( auto_now_add=True)
    update = models.DateTimeField( auto_now=True)

    def __str__(self) -> str:
        return str(self.rating)+"| "+str(self.watchlist.name)