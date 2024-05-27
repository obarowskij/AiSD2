# Generated by Django 4.2.7 on 2024-05-19 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flatworld", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="guard",
            name="steps",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="day",
            name="day",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="day",
            name="person_id",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]