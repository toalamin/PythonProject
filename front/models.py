from django.db import models

# Create your models here.
class Aboutus(models.Model):
    title = models.CharField(max_length=200,blank=False)
    description = models.TextField(max_length=700,blank=False)
    image = models.ImageField(upload_to='about/',blank=False)


    def __str__(self):
        return self.title
    

class Slider(models.Model):
    title = models.CharField(max_length=200,blank=False)
    description = models.TextField(max_length=700,blank=False)
    image = models.ImageField(upload_to='slider/',blank=False)


    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=100,blank=False,default="",null=True)
    link = models.CharField(max_length=200,blank=False)
    image = models.ImageField(upload_to='client/',blank=False)

    def __str__(self):
        return self.name
