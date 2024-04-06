from django.db import models

class MyInfo(models.Model):
    name = models.CharField(max_length=20, default="")
    age = models.IntegerField(default="")
    address = models.CharField(max_length=50, default="")
    phone = models.IntegerField(default="")

    class Meta:
        db_table = 'custom_table_name'  # Specify a custom table name here


# Create your models here.
