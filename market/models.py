from django.db import models

# Django: Importing User Model
from django.contrib.auth.models import User

# Codex: Importing Models
from codex.models import Companion, Warframe, Weapon

class Item(models.Model):
    TIPE_CHOICES = (
        ('C', 'Companion'),
        ('M', 'Mods'),
        ('W', 'Warframe'),
        ('E', 'Weapon'),
    )
    tipe = models.CharField(default='E', max_length=1, choices=TIPE_CHOICES)
    companion = models.ForeignKey(Companion, on_delete=models.CASCADE, null=True, blank=True)
    warframe = models.ForeignKey(Warframe, on_delete=models.CASCADE, null=True, blank=True)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

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
    is_ended = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)