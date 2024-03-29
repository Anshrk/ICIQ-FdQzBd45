# Generated by Django 5.0.2 on 2024-03-02 07:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Garbage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pictures", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("location_link", models.CharField(max_length=200)),
                ("number_of_points", models.IntegerField()),
                ("type_of_garbage", models.CharField(max_length=200)),
                ("where_to_displose", models.TextField(max_length=200)),
            ],
        ),
    ]
