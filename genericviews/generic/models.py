from django.db import models

# Create your models here.


class Game(models.Model):
    Name = models.CharField(max_length=50)
    Cat = models.CharField(max_length=50)
    Users = models.CharField(max_length=50)
    Rating = models.CharField(max_length=50)
    Reviews = models.TextField()

    def __str__(self) -> str:
        return self.Name
