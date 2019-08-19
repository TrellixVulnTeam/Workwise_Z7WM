# Generated by Django 2.2.4 on 2019-08-19 12:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Job', '0009_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view',
            field=models.ManyToManyField(related_name='view_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
