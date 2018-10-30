from django.db import models

# Django: Importing User Model
from django.contrib.auth.models import User

# WFPY: UserProfile reciever and post_save signal: Needed to create a UserProfile objects when the User account its created.
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserProfile(models.Model):
    STATUS_CHOICES = (
        ('O', 'Online'),
        ('I', 'In Game',),
        ('F', 'Offline',),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user/avatar', default='avatar/default.png', blank=True)
    bio = models.CharField(max_length=140, blank=True)
    status = models.CharField(default='F', max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()