from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from accounts.models import Account, Profile


@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


@receiver(post_migrate)
def create_missing_profiles(sender, **kwargs):
    for account in Account.objects.filter(profile=None):
        Profile.objects.get_or_create(user=account)