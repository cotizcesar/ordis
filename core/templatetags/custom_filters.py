import os.path
from datetime import datetime, date, timedelta
import time

from django import template
from django.conf import settings
register = template.Library()
import re

@register.filter(name='youtube_embed_url')
def youtube_embed_url(value):
    # Starting a Div Bootstrap 4 responsive.
    div_responsive_start = '<div class="embed-responsive embed-responsive-16by9">'
    div_responsive_end = '</div>'
    iframe1 = '<iframe class="embed-responsive-item" src="'
    iframe2 = '" allowfullscreen="allowfullscreen" mozallowfullscreen="mozallowfullscreen" msallowfullscreen="msallowfullscreen" oallowfullscreen="oallowfullscreen" webkitallowfullscreen="webkitallowfullscreen"></iframe>'
    nosupp = '<div class="jumbotron bg-black-t">'
    orted = '</div>'
    match = re.search(r'^(?:https?:\/\/)?(?:www\.|m\.)?youtu\.?be(?:\.com)?\/?.*(?:watch|embed)?(?:.*v=|v\/|\/)([\w\-_]+)?(\?t=\d+s)?(&feature=related)?$', value)
    match2 = re.search(r'^(http|https)?:\/\/(www\.)?vimeo.com\/(?:channels\/(?:\w+\/)?|groups\/([^\/]*)\/videos\/|)(\d+)(?:|\/\?)$', value)
    match3 = re.search(r'^(^http(s)?://)?((www|en-es|en-gb|secure|beta|ro|www-origin|en-ca|fr-ca|lt|zh-tw|he|id|ca|mk|lv|ma|tl|hi|ar|bg|vi|th)\.)?twitch.tv/(?!directory|p|user/legal|admin|login|signup|jobs)(?P<channel>\w+)$', value)
    match4 = re.search(r'^(http|https)?:\/\/(www|clips)?.twitch.tv\/(\w+)$', value)
    match5 = re.search(r'^(http|https):\/\/(media|giphy).(com|giphy.com)\/(media|gifs)\/([a-zA-Z0-9_.-]*)\/([a-zA-Z0-9_.-]*)$', value)
    if match:
        embed_url = 'https://www.youtube.com/embed/%s?rel=0' %(match.group(1))
        res = div_responsive_start + iframe1 + embed_url + iframe2 + div_responsive_end
        return res
    elif match2:
        embed_url = 'https://player.vimeo.com/video/%s' %(match2.group(4))
        res = div_responsive_start + iframe1 + embed_url + iframe2 + div_responsive_end
        return res
    elif match3:
        embed_url = 'https://player.twitch.tv/?channel=%s&autoplay=false' %(match3.group('channel'))
        res = div_responsive_start + iframe1 + embed_url + iframe2 + div_responsive_end
        return res
    elif match4:
        embed_url = 'https://clips.twitch.tv/embed?clip=%s&autoplay=false' %(match4.group(3))
        res = div_responsive_start + iframe1 + embed_url + iframe2 + div_responsive_end
        return res
    elif match5:        
        embed_url = 'https://media.giphy.com/media/%s/giphy.mp4' %(match5.group(5))
        res = div_responsive_start + '<video class="embed-responsive-item" autoplay loop><source src="' + embed_url + '" type="video/mp4"></video>' + div_responsive_end
        return res
    else:
        embed_url = '<h2 class="lead text-center">Link format not supported.</h2> <p class="text-center text-info">The developers have been notified of this error.</p>'
        res = nosupp + embed_url + orted
        return res
    return ''

youtube_embed_url.is_safe = True

@register.filter(name='unix_to_readeable')
def unix_to_readeable(value):
    value = value[:-3]
    value = int(value)
    value = datetime.fromtimestamp(value)
    return value

@register.filter(name='human_time')
def human_time(value):
    value = value[:-3]
    value = int(value)
    value = datetime.fromtimestamp(value)
    return value.strftime('%m/%d/%Y %I:%M:%S') # %I:%M:%S MM/DD/YYYY hh:mm:ss

@register.filter(name='hubs_name')
def hubs_name(value):
    if value == 'MercuryHUB':
        return 'Larunda Relay'
    elif value == 'EarthHUB':
        return 'Strata Relay'
    else:
        return '???'

@register.filter(name='factions_name')
def factions_name(value):
    if value == 'FC_INFESTATION':
        return 'Infestation'
    elif value == 'FC_CORPUS':
        return 'Corpus'
    elif value == 'FC_GRINEER':
        return 'Grineer'
    else:
        return '???'

@register.filter(name='mission_name')
def mission_name(value):
    if value == 'MT_DEFENSE':
        return 'Defense'
    elif value == 'MT_HIVE':
        return 'Hive'
    elif value == 'MT_EXTERMINATION':
        return 'Exterminate'
    elif value == 'MT_RESCUE':
        return 'Rescue'
    elif value == 'MT_TERRITORY':
        return 'Interception'
    elif value == 'MT_INTEL':
        return 'Spy'
    elif value == 'MT_MOBILE_DEFENSE':
        return 'Mobile Defense'
    elif value == 'MT_SURVIVAL':
        return 'Survival'
    elif value == 'MT_EVACUATION':
        return 'Defection'
    elif value == 'MT_SABOTAGE':
        return 'Sabotage'
    elif value == 'MT_CAPTURE':
        return 'Capture'
    elif value == 'MT_RETRIEVAL':
        return 'Hijack'
    elif value == 'MT_EXCAVATE':
        return 'Excavation'
        
    else:
        return '???'

@register.filter(name='solnode_name')
def solnode_name(value):
    # Earth
    if value == 'SolNode75':
        return 'Cervantes (Earth)'
    elif value == 'SolNode39':
        return 'Everest (Earth)'

    # Venus    
    elif value == 'SolNode22':
        return 'Tessera (Venus)'
    elif value == 'SolNode23':
        return 'Cytherean (Venus)'
    elif value == 'SolNode107':
        return 'Venera (Venus)'
    
    # Mars
    elif value == 'SolNode68':
        return 'Vallis (Mars)'
    
    # Mercury
    elif value == 'SolNode130':
        return 'Lares (Mercury)'
    elif value == 'SolNode223':
        return 'Boethius (Mercury)'
    elif value == 'SolNode119':
        return 'Caloris (Mercury)'
    
    # Ceres
    elif value == 'SolNode138':
        return 'Ludi (Ceres)'
    elif value == 'SolNode140':
        return 'Kiste (Ceres)'
    elif value == 'SolNode149':
        return 'Casta (Ceres)'

    # Saturn
    elif value == 'SolNode20':
        return 'Telesto (Saturn)'
    elif value == 'SolNode31':
        return 'Anthe (Saturn)'
    elif value == 'SolNode96':
        return 'Titan (Saturn)'
    
    # Europa
    elif value == 'SolNode209':
        return 'Morax (Europa)'
    elif value == 'SolNode211':
        return 'Ose (Europa)'
    elif value == 'SolNode217':
        return 'Orias (Europa)'
    elif value == 'SolNode220':
        return 'Kokabiel (Europa)'        

    # Sedna
    elif value == 'SolNode189':
        return 'Naga (Sedna)'
    elif value == 'SolNode191':
        return 'Marid (Sedna)'
    elif value == 'SolNode196':
        return 'Charybdis (Sedna)'
        
    
    # Pluto
    elif value == 'SolNode43':
        return 'Cerberus (Pluto)'
    elif value == 'SolNode56':
        return 'Cypress (Pluto)'
    
    # Phobos
    elif value == 'SettlementNode2':
        return 'Skyresh (Phobos)'
    elif value == 'SettlementNode3':
        return 'Stickney (Phobos)'
    elif value == 'SettlementNode14':
        return 'Shklovsky (Phobos)'
        
    
    # Eris
    elif value == 'SolNode166':
        return 'Nimus (Eris)'
    
    # Neptune
    elif value == 'SolNode17':
        return 'Proteus (Neptune)'
    elif value == 'SolNode57':
        return 'Sao (Neptune)'
    elif value == 'SolNode84':
        return 'Nereid (Neptune)'
    
    # Jupiter
    elif value == 'SolNode10':
        return 'Thebe (Jupiter)'
    
    # Void
    elif value == 'SolNode412':
        return 'Mithra (Void)'

    # Uranus
    elif value == 'SolNode34':
        return 'Sycorax (Uranus)'
    else:
        return '???'

@register.filter(name='item_name')
def item_name(value):
    if value == '/Lotus/Types/Items/MiscItems/Alertium':
        return 'Nitain Extract'
    elif value == '/Lotus/Types/Items/MiscItems/Gallium':
        return 'Gallium'
    elif value == '/Lotus/Types/Items/MiscItems/NeuralSensor':
        return 'Neural Sensors'
    elif value == '/Lotus/Types/Items/MiscItems/Morphic':
        return 'Morphics'
    elif value == '/Lotus/Types/Items/MiscItems/VoidTearDrop':
        return 'Void Traces'
    elif value == '/Lotus/Types/Items/MiscItems/OxiumAlloy':
        return 'Oxium'
    elif value == '/Lotus/Types/Items/MiscItems/OrokinCell':
        return 'Orokin Cell'
    else:
        return '???'

@register.filter(name='sortie_condition')
def item_name(value):
    if value == 'SORTIE_MODIFIER_HAZARD_COLD':
        return 'Extreme Cold'
    elif value == 'SORTIE_MODIFIER_MAGNETIC':
        return 'Enemy Elemental Enhancement (Magnetic)'
    elif value == 'SORTIE_MODIFIER_PUNCTURE':
        return 'Enemy Physical Enhancement (Puncture)'
    else:
        return '???'