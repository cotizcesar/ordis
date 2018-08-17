from django.db import models

# Django: Importing User Model
from django.contrib.auth.models import User

# WFPY: UserProfile reciever and post_save signal: Needed to create a UserProfile objects when the User account its created.
from django.dispatch import receiver
from django.db.models.signals import post_save

# WFPY: User Profile Model -Start-
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user/avatar', default='avatar/default.png', blank=True)
    header = models.ImageField(upload_to='user/header', default='avatar/default.png', blank=True)
    bio = models.CharField(max_length=140, blank=True)
    website = models.URLField(max_length=200, blank=True)

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

# WFPY: User Profile Model -End-