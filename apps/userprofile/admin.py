from django.contrib import admin

# Register your models here.

# Import Models

from .models import Userprofile

# Register

admin.site.register(Userprofile)