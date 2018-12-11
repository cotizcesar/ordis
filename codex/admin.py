from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Core: Importing Models
from .models import Quest, QuestWalkthrough, Weapon, Stat, Warframe, WarframeAbility

class QuestResource(resources.ModelResource):
    class Meta:
        model = Quest

@admin.register(Quest)
class QuestAdmin(ImportExportModelAdmin):
    pass    

class QuestWalkthroughResource(resources.ModelResource):
    class Meta:
        model = QuestWalkthrough

@admin.register(QuestWalkthrough)
class QuestWalkthroughAdmin(ImportExportModelAdmin):
    pass

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

class WarframeResource(resources.ModelResource):
    class Meta:
        model = Warframe

@admin.register(Warframe)
class WarframeAdmin(ImportExportModelAdmin):
    pass

class WarframeAbilityResource(resources.ModelResource):
    class Meta:
        model = WarframeAbility

@admin.register(WarframeAbility)
class WarframeAbilityAdmin(ImportExportModelAdmin):
    pass