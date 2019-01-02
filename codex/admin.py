from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Core: Importing Models
from .models import ItemAttribute, ItemTipe, Item, ItemAttributeValue, ItemAttributeText, Quest, QuestWalkthrough, Companion, Weapon, Stat, Warframe, WarframeAbility

# ItemAttribute Model
# ItemTipe > ItemAttribute
class ItemAttributeResource(resources.ModelResource):
    class Meta:
        model = ItemAttribute

@admin.register(ItemAttribute)
class ItemAttributeAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    pass 

# ItemTipe Model
# ItemTipe > Item
class ItemTipeResource(resources.ModelResource):
    class Meta:
        model = ItemTipe

@admin.register(ItemTipe)
class ItemTipeAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    pass 

# Item Model
# Item
class ItemResource(resources.ModelResource):
    class Meta:
        model = Item

@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    list_display = ('name', 'slug', 'tipe', 'is_prime', 'is_tradeable')
    list_filter = ('tipe', 'is_prime', 'is_tradeable')
    pass

# ItemAttribute Model
# Item < ItemAttributeValue > ItemAttribute
class ItemAttributeValueResource(resources.ModelResource):
    class Meta:
        model = ItemAttributeValue

@admin.register(ItemAttributeValue)
class ItemAttributeValueAdmin(ImportExportModelAdmin):
    list_display = ('item', 'name', 'value')
    pass 

# ItemAttribute Model
# Item < ItemAttributeText > ItemAttribute
class ItemAttributeTextResource(resources.ModelResource):
    class Meta:
        model = ItemAttributeText

@admin.register(ItemAttributeText)
class ItemAttributeTextAdmin(ImportExportModelAdmin):
    list_display = ('item', 'name', 'value')
    pass 

# --
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