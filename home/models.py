from django.db import models

# Create your models here.
class Volunteer(models.Model):
    v_id=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=122)
    Email = models.CharField(max_length=122)
    Department = models.CharField(max_length=122)
    Phone = models.CharField(max_length=12)
    Volunteer_as = models.CharField(max_length=100)
    date = models.DateField()
    
class Alumni(models.Model):
     a_id=models.AutoField(primary_key=True)
     Name = models.CharField(max_length=122)
     Email = models.CharField(max_length=122)
     Phone = models.CharField(max_length=12)
     Department = models.CharField(max_length=122)
     Abroad= models.CharField(max_length=12)



class Registration(models.Model):
    r_id=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=122)
    Email = models.CharField(max_length=122)
    Department = models.CharField(max_length=12)
    date = models.DateField()
    preference=models.CharField(max_length=100)    