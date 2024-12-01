from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Set up admin roles and permissions'

    def handle(self, *args, **kwargs):
        # Create the groups
        superusers_group, _ = Group.objects.get_or_create(name="Superusers")
        moderators_group, _ = Group.objects.get_or_create(name="Moderators")

        all_permissions = Permission.objects.all()
        superusers_group.permissions.set(all_permissions)  # Assign all permissions

        moderator_permissions = [
            "view_game", "change_game", "delete_review", "add_review", "change_review", "change_review"
        ]

        for codename in moderator_permissions:
            permission = Permission.objects.filter(codename=codename).first()
            if permission:
                moderators_group.permissions.add(permission)
            else:
                self.stderr.write(self.style.WARNING(f"Permission '{codename}' not found!"))

        self.stdout.write(self.style.SUCCESS("Roles and permissions have been successfully set up!"))
