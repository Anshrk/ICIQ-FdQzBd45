# Generated by Django 5.0.2 on 2024-03-02 23:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("garbage", "0005_alter_garbage_number_of_points"),
    ]

    operations = [
        migrations.RenameField(
            model_name="garbage",
            old_name="location_link",
            new_name="location",
        ),
    ]