from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Core: Importing Models
from .models import Quest, QuestWalkthrough, Weapon, Stat

admin.site.register(Quest)
admin.site.register(QuestWalkthrough)
#admin.site.register(Weapon)
#admin.site.register(Stat)

class QuestAdmin(admin.ModelAdmin):
    model = Quest
    list_per_page = 22
    ordering = ('-name',)

class QuestWalkthroughAdmin(admin.ModelAdmin):
    model = QuestWalkthrough
    list_per_page = 22

class WeaponResource(resources.ModelResource):
    class Meta:
        model = Weapon

@admin.register(Weapon)
class WeaponAdmin(ImportExportModelAdmin):
    pass

class StatResource(resources.ModelResource):
    class Meta:
        model = Stat

@admin.register(Stat)
class StatAdmin(ImportExportModelAdmin):
    pass