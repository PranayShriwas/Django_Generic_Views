from django.db import models

# Create your models here.


class Cloths(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.IntegerField()
    Cat = models.CharField(max_length=50)
    Brand = models.CharField(max_length=50)
    Size = models.IntegerField()

    def __str__(self) -> str:
        return self.Name
