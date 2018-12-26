from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Core: Importing Models
from .models import Item, Order

class ItemResource(resources.ModelResource):
    class Meta:
        model = Item

@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    pass

class OrderResource(resources.ModelResource):
    class Meta:
        model = Order

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    pass