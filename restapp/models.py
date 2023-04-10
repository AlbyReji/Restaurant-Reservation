from django.db import models


from django.contrib.auth.models import User

# Create your models here.
class bookingdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    time = models.TimeField()
    date = models.DateField()
    totalpeople = models.CharField(max_length=10)
    class Meta:
        db_table ="bookingdetails"

class contactdetails(models.Model):
    Name = models.CharField(max_length=50)
    Phone = models.CharField(max_length=11)
    Email = models.EmailField()
    Subject = models.TextField(max_length=50)
    class Meta:
        db_table = "contactdetails"
        

class restdetails(models.Model):
    special = models.CharField(max_length=60)
    opentime = models.TimeField()
    closetime = models.TimeField()
    class Meta:
        db_table = "restdetails"