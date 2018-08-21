from django.db import models

class Item(models.Model):
    RARITY_CHOICES = (
        ('P', 'Peculiar'),
        ('C', 'Common',),
        ('U', 'Uncommon',),
        ('R', 'Rare',),
        ('L', 'Legendary',),
        ('I', 'Riven',),
    )
    name = models.CharField(max_length=140)
    slug = models.CharField(max_length=140)
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='item', default='item/default.png', blank=True)
    ducats = models.PositiveIntegerField(blank=True)
    trading_tax = models.PositiveIntegerField()
    mastery_level = models.PositiveIntegerField()
    rarity = models.CharField(max_length=1, choices=RARITY_CHOICES)
    component = models.ForeignKey('self', on_delete=models.CASCADE)
    mod_rank = models.PositiveIntegerField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)