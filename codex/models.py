from django.db import models

class Quest(models.Model):
    name = models.CharField(max_length=140)
    image = models.ImageField(upload_to='codex/quests', default='codex/quests/default.png', blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name