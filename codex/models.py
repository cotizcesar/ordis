from django.db import models

# django-ckeditor: Usage for WYSIWYG fields.
from ckeditor.fields import RichTextField

# ItemAbility Model
# Defines the ability name in the Item Model.
class ItemAbility(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

# ItemAttribute Model
# Defines the attribute name in the Item Model.
class ItemAttribute(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

# ItemTipe Model
# Defines the tipe name in the Item Model.
class ItemTipe(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

# Item Model
# Main Model for Companions, Warframes, Weapons.
class Item(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField()
    tipe = models.ForeignKey(ItemTipe, on_delete=models.CASCADE)
    description = models.TextField(max_length=700)
    image = models.ImageField(upload_to='codex/item', default='codex/item/default.png', blank=True)
    mastery_rank = models.PositiveIntegerField(default=0)
    is_prime = models.BooleanField(default=False)
    is_tradeable = models.BooleanField(default=False)
    release_date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# ItemAttributeValue Model
# Defines the value and name of the item.
class ItemAttributeValue(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.ForeignKey(ItemAttribute, on_delete=models.CASCADE)
    value = models.PositiveIntegerField()

    def __str__(self):
        return self.name.name

# ItemAbilityValue Model
# Defines the value and name of the ability.
class ItemAbilityValue(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.ForeignKey(ItemAbility, on_delete=models.CASCADE)
    value = models.TextField(max_length=210)
    image = models.ImageField(upload_to='codex/item/ability', default='codex/item/ability/default.png', blank=True)

    def __str__(self):
        return self.name.name

class Quest(models.Model):
    TIPE_CHOICES = (
        ('M', 'Main Quest'),
        ('O', 'Optional Quest'),
        ('L', 'Optional Lore Quest'),
    )
    name = models.CharField(max_length=140)
    tipe = models.CharField(default='M', max_length=1, choices=TIPE_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='codex/quests', default='codex/quests/default.png', blank=True)
    slug = models.SlugField()
    quest_order = models.PositiveIntegerField(null=True, blank=True)
    is_replayable = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['quest_order']

    def __str__(self):
        return self.name

class QuestWalkthrough(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    name = models.CharField(max_length=140)
    description = RichTextField()

    class Meta:
        ordering = ['-quest']

    def __str__(self):
        return self.quest.name + ' > ' + self.name
