#from django.contrib import admin

# Core: Importing Models
#from .models import Quest, Weapon, Stat

#admin.site.register(Quest)
#admin.site.register(Weapon)
#admin.site.register(Stat)

from import_export import resources
from .models import Quest, Weapon, Stat

class QuestResource(resources.ModelResource):

    class Meta:
        model = Quest
        
class WeaponResource(resources.ModelResource):

    class Meta:
        model = Weapon

class StatResource(resources.ModelResource):

    class Meta:
        model = Stat