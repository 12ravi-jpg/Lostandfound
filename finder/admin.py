from django.contrib import admin
from .models import CustomUser, Item

# This registers your models so you can see them in the admin panel
admin.site.register(CustomUser)
admin.site.register(Item)