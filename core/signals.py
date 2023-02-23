from django.contrib.auth.models import User
from django.db.models.signals import post_save

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(usuario=instance)
    
    print('Signal chamado com sucesso')


post_save.connect(create_profile, sender=User)