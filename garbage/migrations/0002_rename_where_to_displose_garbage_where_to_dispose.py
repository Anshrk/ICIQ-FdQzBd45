# Generated by Django 5.0.2 on 2024-03-02 07:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("garbage", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="garbage",
            old_name="where_to_displose",
            new_name="where_to_dispose",
        ),
    ]