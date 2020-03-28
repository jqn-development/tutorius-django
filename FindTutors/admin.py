from django.contrib import admin

# Register your models here.
from .models import TUser, Profile

admin.site.register(TUser)
admin.site.register(Profile)