# Generated by Django 4.2.20 on 2025-04-29 17:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Articles",
            new_name="Article",
        ),
    ]
