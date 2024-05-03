# Generated by Django 4.2.4 on 2024-04-13 20:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.TextField(
                choices=[
                    ("creator", "creator"),
                    ("business", "business"),
                    ("user", "user"),
                ]
            ),
        ),
    ]