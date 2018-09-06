from django.contrib import admin

# Core: Importing Models
from .models import Quest, Weapon, Stat

admin.site.register(Quest)
admin.site.register(Weapon)
admin.site.register(Stat)