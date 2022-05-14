from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

from .models import ModelContact, Subscriber


class ModelContactAdmin(ModelAdmin):
    model = ModelContact
    menu_label = "Contact Forms"
    menu_icon = "mail"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('date_added', 'full_name',
                    "phone_number", "business", 'message')
    search_fields = ("email", "full_name",)

    def full_name(self, ModelContact):
        return f'{ModelContact.first_name} {ModelContact.last_name}'

modeladmin_register(ModelContactAdmin)

class SubscriberAdmin(ModelAdmin):
    model = Subscriber
    menu_label = "Subscribers Forms"
    menu_icon = "group"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('date_added', 'status', 'email',
                    "active")
    search_fields = ("email")

    def status(self, Subscriber):
        if Subscriber.active:
            return  'Active Subscription'
        else:
            return  'Cancelled Subscription'

modeladmin_register(SubscriberAdmin)
