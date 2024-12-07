
from django.core.mail import send_mail
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver

from GameExplorer import settings
from accounts.models import Account, Profile


@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
        send_mail(
            subject='Welcome to GameExplorer!',
            message=f'Hello, {instance.username}! You have created an account on GameExplorer. We are happy to see you on board!',
            from_email=settings.COMPANY_EMAIL,
            recipient_list=[instance.email],
            fail_silently=False,
        )


@receiver(post_migrate)
def create_missing_profiles(sender, **kwargs):
    for account in Account.objects.filter(profile=None):
        Profile.objects.get_or_create(user=account)