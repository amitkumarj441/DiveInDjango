from django.db import models

class Address(models.Model):
  address=models.CharField(max_length=255,blank=True)
  city=models.CharField(max_length=150,blank=True)
  state=models.CharField(max_length=2,blank=True)     // Such as US for Unitet States of America, IN for India
  pin=models.CharField(max_length=15,blank=True)
  
class Contact(models.Model):
  first_name=models.CharField(max_length=255,blank=True)
  last_name=models.CharField(max_length=255,blank=True)
  email=models.EmailField(blank=True)
  phone=models.CharField(max_length=150,blank=True)
  birthdate=models.CharField(auto_now_add=True)
  
  address=models.ForeignKey(Address,null=True)
