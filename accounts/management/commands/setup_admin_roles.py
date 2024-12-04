from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = 'Set up admin roles and permissions'

    def handle(self, *args, **kwargs):
        superusers_group, _ = Group.objects.get_or_create(name="Superusers")
        moderators_group, _ = Group.objects.get_or_create(name="Moderators")

        all_permissions = Permission.objects.all()
        superusers_group.permissions.set(all_permissions)  # Assign all permissions

        # Define permissions by their full name
        moderator_permissions_full_name = [
            "Games | review | Can add review",
            "Games | review | Can view review",
            "Games | review | Can delete review",
        ]

        for perm_full_name in moderator_permissions_full_name:
            try:
                app_label, model, name = [part.strip() for part in perm_full_name.split("|")]

                permission = Permission.objects.filter(
                    content_type__app_label=app_label.lower(),
                    content_type__model=model.lower(),
                    name=name.strip()
                ).first()

                if permission:
                    moderators_group.permissions.add(permission)
                    self.stdout.write(self.style.SUCCESS(f"Added permission: {perm_full_name}"))
                else:
                    self.stderr.write(self.style.WARNING(f"Permission '{perm_full_name}' not found!"))

            except ValueError:
                self.stderr.write(self.style.ERROR(f"Invalid format for permission: {perm_full_name}"))

        self.stdout.write(self.style.SUCCESS("Roles and permissions have been successfully set up!"))
