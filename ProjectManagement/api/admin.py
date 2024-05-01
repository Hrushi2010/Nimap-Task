from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Client

admin.site.register(Client)


# admin.py

from django.contrib import admin
from .models import Client, Project

# admin.site.register(Client)
# admin.site.register(Project)


# # admin.py

# from django.contrib import admin
# from .models import Client, Project

# Unregister Client model if already registered
admin.site.unregister(Client)

# Register Client and Project models
admin.site.register(Client)
admin.site.register(Project)
