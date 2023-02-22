from django.db import models

# Create your models here.
class Contact(models.Model):
   firstname=models.CharField(max_length=30)
   lastname=models.CharField(max_length=30)
   phoneno=models.CharField(max_length=10)
   email=models.CharField(max_length=30)
   comment=models.TextField()
   def __str__(self):
      return self.firstname
   
class Order(models.Model):
   crop=models.CharField(max_length=30)
   quantity=models.CharField(max_length=30)
   date=models.CharField(max_length=30)
   fullname=models.CharField(max_length=30)
   phoneno=models.CharField(max_length=10)
   address=models.CharField(max_length=30)
   
   def __str__(self):
      return self.crop