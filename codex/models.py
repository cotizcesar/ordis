from django.db import models

class Quest(models.Model):
    TIPE_CHOICES = (
        ('M', 'Main Quest'),
        ('O', 'Optional Quest'),
        ('L', 'Optional Lore Quest'),
    )
    name = models.CharField(max_length=140)
    tipe = models.CharField(default='M', max_length=1, choices=TIPE_CHOICES)
    description = models.TextField(default='Description in progress...')
    image = models.ImageField(upload_to='codex/quests', default='codex/quests/default.png', blank=True)
    slug = models.SlugField()
    previous_quest = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='prv_quest')
    next_quest = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='nxt_quest')
    is_replayable = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class QuestWalkthrough(models.Model):
    quest = models.OneToOneField('Quest', on_delete=models.CASCADE)
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=5000)