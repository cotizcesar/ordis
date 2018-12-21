"""wfpy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

# userprofile: Importing Views
from .views import Codex, Quests, QuestDetail, Companions, Universe, Weapons, WeaponsPrimary, WeaponsSecondary, WeaponsMelee, WeaponDetail, Warframes, WarframeDetail

urlpatterns = [
    path('codex/', Codex.as_view(), name='codex'),
    path('codex/quests', Quests.as_view(), name='codex_quests'),
    url(r'codex/quests/(?P<slug>[-\w]+)$', QuestDetail.as_view(), name='codex_quest_detail'),
    path('codex/universe', Universe.as_view(), name='codex_universe'),
    path('codex/universe/companions', Companions.as_view(), name='codex_universe_companions'),
    path('codex/universe/weapons', Weapons.as_view(), name='codex_universe_weapons'),
    path('codex/universe/weapons/primary', WeaponsPrimary.as_view(), name='codex_universe_weapons_primary'),
    path('codex/universe/weapons/secondary', WeaponsSecondary.as_view(), name='codex_universe_weapons_secondary'),
    path('codex/universe/weapons/melee', WeaponsMelee.as_view(), name='codex_universe_weapons_melee'),
    url(r'codex/universe/weapon/(?P<slug>[-\w]+)$', WeaponDetail.as_view(), name='codex_universe_weapon_detail'),
    path('codex/universe/warframes', Warframes.as_view(), name='codex_universe_warframes'),
    url(r'codex/universe/warframe/(?P<slug>[-\w]+)$', WarframeDetail.as_view(), name='codex_universe_warframe_detail'),
]