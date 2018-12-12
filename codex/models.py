from django.db import models

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
    previous_quest = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='prv_quest')
    next_quest = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='nxt_quest')
    is_replayable = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class QuestWalkthrough(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    name = models.CharField(max_length=140)
    description = models.TextField()

    class Meta:
        ordering = ['quest']

    def __str__(self):
        return self.quest.name + ' > ' + self.name

class Weapon(models.Model):
    TIPE_CHOICES = (
        ('P', 'Primary Weapon'),
        ('S', 'Secondary Weapon'),
        ('M', 'Melee Weapon'),
    )
    name = models.CharField(max_length=140)
    slug = models.SlugField()
    image = models.ImageField(upload_to='codex/weapons', default='codex/weapons/default.png', blank=True)
    tipe = models.CharField(default='P', max_length=1, choices=TIPE_CHOICES)
    description = models.TextField(max_length=600)
    mastery_rank = models.PositiveIntegerField(null=True, blank=True)
    is_tradeable = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Stat(models.Model):
    # TODO:
    # falloff (field): (Tratando de ver que hacer) / fuck 2 numeros decimal 1 digito
    TIPE_CHOICES = (
        ('Ac', 'Active'),
        ('Au', 'Auto'),
        ('Ai', 'Air Burst'),
        ('Ba', 'Barrage'),
        ('Be', 'Beacon'),
        ('Bu', 'Buckshot'),
        ('Br', 'Burst'),
        ('Bs', 'Burst Shot'),
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
        ('T', 'Active'),
        ('A', 'Auto'),
        ('B', 'Burst'), 
        ('C', 'Charge'),
        ('D', 'Duplex'),
        ('H', 'Held'),
        ('S', 'Semi'),
    )
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, null=True)
    tipe = models.CharField(default='Pr', max_length=2, choices=TIPE_CHOICES)

    accuracy = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True) # decimal 1 digito
    attack_speed = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True) # decimal 3 digitos
    channeling_cost = models.PositiveIntegerField(blank=True, null=True) # entero
    channeling_damage = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True) # decimal 1 digito con x
    charge_rate = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True) # decimal 2 digitos
    critical_chance = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True) # decimal 1 digito con %
    critical_multiplier = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True) # decimal 1 digito con x
    fall_off_start = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito
    fall_off_end = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito
    damage_block = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True) # decimal 1 digito con %
    fire_rate = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True) # decimal 2 digitos
    leap_attack = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True) # decimal 1 digito
    magazine = models.PositiveIntegerField(blank=True, null=True) # Entero
    noise = models.BooleanField() # lista por ahora un bool.
    punch_through = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True) # decimal 1 digito
    rload = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True) # decimal 1 digito
    spin_attack = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True) # decimal 1 digito
    status = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True) # decimal 1 digito con %
    trigger = models.CharField(max_length=1, choices=TRIGGER_CHOICES, blank=True, null=True) # lista
    per_stack_start = models.PositiveIntegerField(blank=True, null=True) # Entero
    per_stack_end = models.PositiveIntegerField(blank=True, null=True) # Entero
    wall_attack = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True) # decimal 1 digito

    # Status: Normal
    puncture = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito
    impact = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) # decimal 1 digito
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

    class Meta:
        ordering = ['weapon']

    def __str__(self):
        return self.weapon.name + ' > ' + self.tipe

class Warframe(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField()
    description = models.TextField(max_length=280)
    mastery_rank = models.PositiveIntegerField(null=True, blank=True)
    is_prime = models.BooleanField(default=False)
    image = models.ImageField(upload_to='codex/warframe', default='codex/warframe/default.png', blank=True)
    pasive = models.TextField(max_length=280)
    armor = models.PositiveIntegerField()
    energy = models.PositiveIntegerField()
    health = models.PositiveIntegerField()
    shield = models.PositiveIntegerField()
    sprint_speed = models.DecimalField(max_digits=3, decimal_places=2)
    release_date = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class WarframeAbility(models.Model):
    warframe = models.ForeignKey(Warframe, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    slug = models.SlugField()
    description = models.TextField(max_length=140)
    image = models.ImageField(upload_to='codex/warframe/ability', default='codex/warframe/ability/default.png', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['warframe']

    def __str__(self):
        return self.warframe.name + ' > ' + self.name
