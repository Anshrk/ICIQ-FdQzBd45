# Generated by Django 5.0.2 on 2024-03-02 13:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("garbage", "0003_garbage_cleaned_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="garbage",
            name="cleaned",
            field=models.BooleanField(default=False),
        ),
    ]
