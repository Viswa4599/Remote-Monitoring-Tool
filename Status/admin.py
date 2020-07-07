from django.contrib import admin
from .models import CPU,RAM,Network,Clock

# Register your models here.

admin.site.register(CPU)

admin.site.register(RAM)

admin.site.register(Network)

admin.site.register(Clock)