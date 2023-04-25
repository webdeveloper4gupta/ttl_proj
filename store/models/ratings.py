from django.db import models

class Ratings(models.Model):
    name= models.TextField()
    rating=models.IntegerField(max_length=50)
    prodid=models.CharField(max_length=500)
    def __str__(self):
        return self.name