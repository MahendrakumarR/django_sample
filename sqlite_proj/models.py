from django.db import models

class MyInfo(models.Model):
    Name = models.CharField(max_length=20, default="")
    Age = models.IntegerField(default="")
    Address = models.CharField(max_length=50, default="")
    Phone = models.IntegerField(default="")

    class Meta:
        db_table = 'custom_table_name'  # Specify a custom table name here


# Create your models here.
