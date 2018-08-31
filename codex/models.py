from django.db import models

class Quest(models.Model):
    TIPE_CHOICES = (
        ('M', 'Main Quest'),
        ('O', 'Optional Quest'),
        ('L', 'Optional Lore Quest'),
    )
    name = models.CharField(max_length=140)
    tipe = models.CharField(default='M', max_length=1, choices=TIPE_CHOICES)
    description = models.TextField(max_length=5000, null=True)
    overview = models.TextField(max_length=5000, null=True)
    image = models.ImageField(upload_to='codex/quests', default='codex/quests/default.png', blank=True)
    slug = models.SlugField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name