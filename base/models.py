from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()
    phone = models.CharField(max_length=10)
    adress = models.CharField(max_length=200)



    def __str__(self):
        return self.name
