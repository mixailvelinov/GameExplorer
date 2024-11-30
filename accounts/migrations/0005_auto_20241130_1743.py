from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def create_groups(apps, schema_editor):
    # Define your groups
    group_full_crud, created = Group.objects.get_or_create(name="Full CRUD Admins")
    group_limited_crud, created = Group.objects.get_or_create(name="Moderators")

    # Define the permissions
    permission_add_game = Permission.objects.filter(codename="add_game").first()
    permission_change_game = Permission.objects.filter(codename="change_game").first()
    permission_delete_game = Permission.objects.filter(codename="delete_game").first()

    permission_add_review = Permission.objects.filter(codename="add_review").first()
    permission_change_review = Permission.objects.filter(codename="change_review").first()
    permission_delete_review = Permission.objects.filter(codename="delete_review").first()

    if not all([permission_add_game, permission_change_game, permission_delete_game,
                permission_add_review, permission_change_review, permission_delete_review]):
        raise ValueError("Some permissions do not exist. Please check if they have been created.")

    # Assign permissions to the groups
    group_full_crud.permissions.add(
        permission_add_game, permission_change_game, permission_delete_game,
        permission_add_review, permission_change_review, permission_delete_review
    )
    group_limited_crud.permissions.add(
        permission_change_game, permission_add_review, permission_change_review, permission_delete_review
    )


def remove_groups(apps, schema_editor):
    # Clean up groups if needed
    Group.objects.filter(name="Full CRUD Admins").delete()
    Group.objects.filter(name="Moderators").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_account_email'),
    ]

    operations = [
        migrations.RunPython(create_groups, remove_groups),
    ]
