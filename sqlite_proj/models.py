from django.db import models


class Datas(models.Model):    # here create a new class for storing values to database
    Name = models.CharField(max_length=20, default="")
    Age = models.IntegerField(max_length=20, default="")
    Address = models.CharField(max_length=50, default="")
    Phone = models.IntegerField(max_length=20, default="")
    




# Create your models here.
