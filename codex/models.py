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

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.name

class QuestWalkthrough(models.Model):
    quest = models.OneToOneField('Quest', on_delete=models.CASCADE)
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=5000)

class Weapon(models.Model):
    TIPE_CHOICES = (
        ('P', 'Primary Weapon'),
        ('S', 'Secondary Weapon'),
        ('M', 'Melee Weapon'),
    )
    name = models.CharField(max_length=140)
    slug = models.SlugField()
    image = models.ImageField(upload_to='weapons', default='weapons/default.png', blank=True)
    tipe = models.CharField(default='P', max_length=1, choices=TIPE_CHOICES)
    description = models.TextField(max_length=600)
    mastery_rank = models.PositiveIntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Stat(models.Model):
    # TODO:
    # falloff (field): (Tratando de ver que hacer) / fuck 2 numeros decimal 1 digito
    TIPE_CHOICES = (
        ('Au', 'Auto'),
        ('Ai', 'Air Burst'),
        ('Ba', 'Barrage'),
        ('Be', 'Beacon'),
        ('Bu', 'Buckshot'),
        ('Bu', 'Burst'),
        ('Br', 'Burst Shot'),
        ('Ca', 'Cannon'),
        ('Ch', 'Charge'),
        ('Cr', 'Charged Throw'),
        ('Di', 'Disc'),
        ('El', 'Electric Quill'),
        ('Fi', 'Fire Quill'),
        ('Ha', 'Harpoon'),
        ('Ho', 'Horizontal Spread'),
        ('Ic', 'Ice Quill'),
        ('Me', 'Melee'),
        ('Po', 'Poison Quill'),
        ('Pr', 'Primary'),
        ('Se', 'Secondary'),
        ('Sm', 'Semi'),
        ('Sl', 'Slug'),
        ('Th', 'Throw'),
        ('Ve', 'Vertical Spread'),        
    )
    TRIGGER_CHOICES = (
        ('A', 'Auto'),
        ('B', 'Burst'), 
        ('C', 'Charge'),
        ('H', 'Held'),
        ('S', 'Semi'),
    )
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, null=True)
    tipe = models.CharField(default='Pr', max_length=2, choices=TIPE_CHOICES)

    # Primary / Secondary
    accuracy = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True) # decimal 1 digito
    charge_rate = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True) # decimal 2 digitos   
    fire_rate = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True) # decimal 2 digitos
    magazine = models.PositiveIntegerField(blank=True, null=True) # Entero
    noise = models.BooleanField() # lista por ahora un bool.
    punch_through = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True) # decimal 1 digito
    rload = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True) # decimal 1 digito
    trigger = models.CharField(max_length=1, choices=TRIGGER_CHOICES, blank=True, null=True) # lista

    # Melee Stats
    attack_speed = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True) # decimal 3 digitos
    channeling_cost = models.PositiveIntegerField(blank=True, null=True) # entero
    channeling_damage = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True) # decimal 1 digito con x
    damage_block = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True) # decimal 1 digito con %
    leap_attack = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True) # decimal 1 digito
    spin_attack = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True) # decimal 1 digito
    wall_attack = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True) # decimal 1 digito

    # Primary / Secondary / Melee - Stats     
    critical_chance = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True) # decimal 1 digito con %
    critical_multiplier = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True) # decimal 1 digito con x
    status = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True) # decimal 1 digito con %

    # Status: Normal
    impact = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito
    puncture = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito
    slash = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito

    # Status: Normal
    cold = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito
    electricity = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito
    heat = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito
    toxin = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito
    void = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito

    # Status: Combined, Damage 2.0
    blast = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito
    corrosive = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito
    gas = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito
    magnetic = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito
    radiation = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito
    viral = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito

    def __str__(self):
        return self.weapon.name + ' > ' + self.tipe