# Generated by Django 5.0 on 2024-01-13 04:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_listing_watch_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='watch_list',
            field=models.ManyToManyField(blank=True, null=True, related_name='userOFwatchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
