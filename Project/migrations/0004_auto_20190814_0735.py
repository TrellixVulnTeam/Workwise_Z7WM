# Generated by Django 2.2.4 on 2019-08-14 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Project', '0003_auto_20190813_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='categories_fields', to='Project.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='like_project', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
