from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

from .models import SiteManagerSetting


class SiteManagerSettingAdmin(ModelAdmin):
    model = SiteManagerSetting
    menu_label = "SiteManager Setting"
    menu_icon = ["home"]
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('businessname', 'address',
                    "location", "phone", 'email', 'email_thank_you_text')
 

    def full_name(self, ModelContact):
        return f'{ModelContact.first_name} {ModelContact.last_name}'


'''
 businessname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=100) 
    email = models.CharField(max_length=100) 
    email_thank_you_text = models.TextField()

'''
modeladmin_register(SiteManagerSettingAdmin)