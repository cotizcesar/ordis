from django.contrib import admin

# Core: Importing Models
from .models import Quest, QuestWalkthrough, Weapon, Stat

admin.site.register(Quest)
admin.site.register(QuestWalkthrough)
admin.site.register(Weapon)
admin.site.register(Stat)

class QuestAdmin(admin.ModelAdmin):
    model = Quest
    list_per_page = 22

class QuestWalkthroughAdmin(admin.ModelAdmin):
    model = QuestWalkthrough
    list_per_page = 22

class WeaponAdmin(admin.ModelAdmin):
    model = Weapon
    list_per_page = 22

class StatAdmin(admin.ModelAdmin):
    model = Stat
    list_per_page = 22