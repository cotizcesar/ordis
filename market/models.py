from django.db import models

# Django: Importing User Model
from django.contrib.auth.models import User

# Codex: Importing Models
from codex.models import Warframe, Weapon

class Item(models.Model):
    RARITY_CHOICES = (
        ('P', 'Peculiar'),
        ('C', 'Common',),
        ('U', 'Uncommon',),
        ('R', 'Rare',),
        ('L', 'Legendary',),
        ('I', 'Riven',),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=140)
    slug = models.SlugField()
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='item', default='item/default.png', blank=True)
    ducats = models.PositiveIntegerField(null=True, blank=True)
    trading_tax = models.PositiveIntegerField()
    mastery_rank = models.PositiveIntegerField()
    rarity = models.CharField(max_length=1, choices=RARITY_CHOICES, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    WANT_CHOICES = (
        ('S', 'Sell'),
        ('B', 'Buy',),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    want = models.CharField(default='S', max_length=1, choices=WANT_CHOICES)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    mod_rank = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_ended = models.BooleanField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '(@' +self.user.username + '): ' + self.want + ' > ' + self.item.name