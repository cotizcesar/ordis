from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Core: Importing Models
from .models import Quest, QuestWalkthrough, Companion, Weapon, Stat, Warframe, WarframeAbility

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

class CompanionResource(resources.ModelResource):
    class Meta:
        model = Companion

@admin.register(Companion)
class CompanionAdmin(ImportExportModelAdmin):
    list_display = ('name', 'slug', 'is_tradeable', 'is_prime')
    pass

class WeaponResource(resources.ModelResource):
    class Meta:
        model = Weapon

@admin.register(Weapon)
class WeaponAdmin(ImportExportModelAdmin):
    list_display = ('name', 'slug', 'is_tradeable', 'is_prime')
    pass

class StatResource(resources.ModelResource):
    class Meta:
        model = Stat

@admin.register(Stat)
class StatAdmin(ImportExportModelAdmin):
    pass

class WarframeResource(resources.ModelResource):
    fields = ['name', 'slug']
    class Meta:
        model = Warframe

@admin.register(Warframe)
class WarframeAdmin(ImportExportModelAdmin):
    list_display = ('name', 'slug', 'is_tradeable', 'is_prime')
    pass

class WarframeAbilityResource(resources.ModelResource):
    class Meta:
        model = WarframeAbility

@admin.register(WarframeAbility)
class WarframeAbilityAdmin(ImportExportModelAdmin):
    pass