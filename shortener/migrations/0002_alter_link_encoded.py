# Generated by Django 4.1.5 on 2023-01-18 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='encoded',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
