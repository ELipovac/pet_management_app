from django.contrib import admin
from .models import Pet, VeterinaryService

admin.site.register(Pet)
admin.site.register(VeterinaryService)