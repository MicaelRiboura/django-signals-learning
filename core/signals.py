from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Profile

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(usuario=instance)
    elif not hasattr(instance, 'profile'):
            Profile.objects.create(usuario=instance)


post_save.connect(create_profile, sender=User)