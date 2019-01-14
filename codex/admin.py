from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Core: Importing Models
from .models import Item, ItemTipe, ItemAttribute, ItemAttributeValue, ItemAbility, ItemAbilityValue, Quest, QuestWalkthrough

# Item Model
# Item
class ItemResource(resources.ModelResource):
    class Meta:
        model = Item

@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    list_display = ('name', 'slug', 'tipe', 'image', 'is_prime', 'is_tradeable', 'release_date')
    list_filter = ('tipe', 'is_prime', 'is_tradeable')
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

# ItemAttribute Model
# ItemTipe > ItemAttribute
class ItemAttributeResource(resources.ModelResource):
    class Meta:
        model = ItemAttribute

@admin.register(ItemAttribute)
class ItemAttributeAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    pass 

# ItemAttributeValue Model
# Item < ItemAttributeValue > ItemAttribute
class ItemAttributeValueResource(resources.ModelResource):
    class Meta:
        model = ItemAttributeValue

@admin.register(ItemAttributeValue)
class ItemAttributeValueAdmin(ImportExportModelAdmin):
    list_display = ('item', 'name', 'value')
    pass 

# ItemAbility Model
# ItemTipe > ItemAbility
class ItemAbilityResource(resources.ModelResource):
    class Meta:
        model = ItemAbility

@admin.register(ItemAbility)
class ItemAbilityAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    pass 

# ItemAbilityValue Model
# Item < ItemAbilityValue > ItemAttribute
class ItemAbilityValueResource(resources.ModelResource):
    class Meta:
        model = ItemAbilityValue

@admin.register(ItemAbilityValue)
class ItemAbilityValueAdmin(ImportExportModelAdmin):
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