from turtle import title
from django.db import models

# Create your models here.
#salam page models**************************************************






#salam site elements
class salam (models.Model):
    page = models.CharField(max_length=50,blank=True, null=True)
    elements = models.CharField(max_length=50,blank=True, null=True)
    title = models.CharField(max_length=50,blank=True, null=True)
    subtitle = models.CharField(max_length=500,blank=True, null=True)
    link = models.CharField(max_length=500,blank=True, null=True)
    text = models.TextField(max_length=5000,blank=True)
    text2 = models.TextField(max_length=5000,blank=True)
    image = models.ImageField(blank=True, null=True)

class AUTIP (models.Model):
    title = models.CharField(max_length=50,blank=True, null=True)
    subtitle = models.CharField(max_length=50,blank=True, null=True)
    text = models.CharField(max_length=2000,blank=True, null=True)
    def __str__(self):
        return self.title
#Portfolio Modals
class Portfolio_Modals (models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    text = models.TextField(max_length=5000,blank=True)



class Registration(models.Model):
    fname = models.CharField(max_length=50,blank=True, null=True)
    lname = models.CharField(max_length=50,blank=True, null=True)
    email = models.CharField(max_length=120,blank=True, null=True)
    phoneno = models.CharField(max_length=20,blank=True, null=True)
    pirthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    level = models.CharField(max_length=200,blank=True, null=True)

class blog(models.Model):
    title = models.CharField(max_length=100)
    pragrapg1 = models.CharField(max_length=5000,blank=True, null=True)
    pragrapg2 = models.CharField(max_length=5000,blank=True, null=True)
    pragrapg4 = models.CharField(max_length=5000,blank=True, null=True)
    pragrapg5 = models.CharField(max_length=5000,blank=True, null=True)
    pragrapg6 = models.CharField(max_length=5000,blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)

class why(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    pragrapg1 = models.CharField(max_length=5000,blank=True)
    pragrapg2 = models.CharField(max_length=5000,blank=True)
    image = models.ImageField(blank=True, null=True)

class homeslids(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    pragrapg = models.TextField(max_length=5000,blank=True)
    link = models.CharField(max_length=1000,blank=True)
    image = models.ImageField(blank=True, null=True)

class news(models.Model):
    title = models.CharField(max_length=1500,blank=True, null=True)
    pragrapg = models.CharField(max_length=5000,blank=True)
    day = models.CharField(max_length=5,blank=True)
    month = models.CharField(max_length=5,blank=True)
    link = models.CharField(max_length=1000,blank=True)
    image = models.ImageField(blank=True, null=True)

class faculty_members (models.Model):
    name = models.CharField(max_length=1000,blank=True)
    jop= models.CharField(max_length=1000,blank=True)
    image = models.ImageField(blank=True, null=True)
    degree= models.CharField(max_length=1000,blank=True)
    facebook = models.CharField(max_length=1500,blank=True)
    twitter = models.CharField(max_length=1500,blank=True)
    linkedin = models.CharField(max_length=1500,blank=True)


class images (models.Model):
    image = models.ImageField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=500,blank=True)
    text = models.CharField(max_length=5000,blank=True)

class aboutprogram (models.Model):
    name = models.CharField(max_length=5000,blank=True)
