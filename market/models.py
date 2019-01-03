from django.db import models

# Django: Importing User Model
from django.contrib.auth.models import User

# Codex: Importing Models
from codex.models import Item

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