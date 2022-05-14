from concurrent.futures.process import _python_exit
from ctypes import addressof
from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from  wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
# Create your models here.
@register_setting
class SocialMediaSetting(BaseSetting):
    facebook = models.URLField(max_length=250, null=True, blank=True) 
    twitter = models.URLField(max_length=250, null=True, blank=True)
    instagram = models.URLField(max_length=250, null=True, blank=True)
    pinterest = models.URLField(max_length=250, null=True, blank=True)
    whatsApp = models.URLField(max_length=250, null=True, blank=True)
    linkedin = models.URLField(max_length=250, null=True, blank=True)


    panels =  [        
        MultiFieldPanel([            
            FieldPanel('facebook'),
            FieldPanel('twitter'),
            FieldPanel('instagram'),
            FieldPanel('pinterest'),
            FieldPanel('whatsApp'),
            FieldPanel('linkedin'),

        ], heading='Social Media Settings'),
    ]




class SiteManagerSetting(models.Model):
    businessname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=100) 
    email = models.CharField(max_length=100) 
    email_thank_you_text = models.TextField()


    panels =  [
        MultiFieldPanel([
            FieldPanel('businessname'),
            FieldPanel('address'),
            FieldPanel('location'),
            FieldPanel('phone'),
            FieldPanel('email'),           
            FieldPanel('email_thank_you_text'),

        ], heading='Business Details'),
      
    ]

    def __str__(self):
        return self.businessname