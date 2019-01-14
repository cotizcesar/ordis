from django.db import models

# Django: Importing User Model
from django.contrib.auth.models import User

# Core: UserProfile reciever and post_save signal: Needed to create a UserProfile objects when the User account its created.
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserProfile(models.Model):
    STATUS_CHOICES = (
        ('O', 'Online'),
        ('I', 'In Game',),
        ('F', 'Offline',),
    )
    PLATFORM_CHOICES = (
        ('PC', 'PC'),
        ('PS4', 'Playstation 4',),
        ('XB1', 'Xbox One',),
        ('NSW', 'Nintendo Switch',),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user/avatar', default='user/avatar/default.png', blank=True)
    bio = models.TextField(max_length=140, blank=True)
    status = models.CharField(default='F', max_length=1, choices=STATUS_CHOICES)
    platform = models.CharField(default='PC', max_length=3, choices=PLATFORM_CHOICES)
    is_verified = models.BooleanField(default=False)
    is_alpha_tester = models.BooleanField(default=False)
    
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
    
# Core: Connection Model.
class Connection(models.Model):
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.PROTECT)
    following = models.ForeignKey(User, related_name='following', on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} : {}".format(self.follower.username, self.following.username)

# Core: Post Model.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=280)
    image = models.ImageField(upload_to='user/post', blank=True)
    video = models.URLField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return "{} {} (@{}) : {}".format(self.user.first_name, self.user.last_name, self.user.username, self.text)

# Core: Comment Model.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=280)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["date_created"]

    def __str__(self):
        return self.text