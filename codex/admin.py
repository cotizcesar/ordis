from django.contrib import admin

# Core: Importing Models
#from .models import Quest

#admin.site.register(Quest)

from import_export.admin import ImportExportModelAdmin
from .models import Quest

@admin.register(Quest)
class QuestAdmin(ImportExportModelAdmin):
    pass