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
    slug = models.SlugField()
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='item', default='item/default.png', blank=True)
    ducats = models.PositiveIntegerField(null=True, blank=True)
    trading_tax = models.PositiveIntegerField()
    mastery_level = models.PositiveIntegerField()
    rarity = models.CharField(max_length=1, choices=RARITY_CHOICES, blank=True)
    main = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    mod_rank = models.PositiveIntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
