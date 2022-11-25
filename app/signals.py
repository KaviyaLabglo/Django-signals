# code
from django.db.models.signals import post_save, pre_delete, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(pre_save, sender=Profile)
def create_profile(sender, instance,**kwargs):
	print('presave')

@receiver(post_save, sender=Profile)
def save_profile(sender, instance, **kwargs):
	#instance.profile.save()
	print('postsave')



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()
	print('post_save')





@receiver(pre_save, sender=User)
def checker(sender, instance, **kwargs):
	print('pre_save')


