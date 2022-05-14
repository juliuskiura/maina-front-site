from pyexpat import model
from django.db import models

# Create your models here.

class Subscriber(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=100) 
    active = models.BooleanField(default=True)   

    def __str__(self):
        return self.email

class ModelContact(models.Model):   
    date_added = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    e_mail = models.EmailField(max_length=100)    
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    business = models.CharField(max_length=100)
    message = models.TextField()


    def __str__(self):
        return f'{self.first_name} {self.first_name}'
    @property
    def full_name(self):
        return f'{self.first_name} {self.first_name}'