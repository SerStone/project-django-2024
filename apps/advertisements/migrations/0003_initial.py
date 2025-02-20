# Generated by Django 5.0.6 on 2024-07-07 17:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('advertisements', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisementmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='advertisementviewlog',
            name='advertisement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='view_logs', to='advertisements.advertisementmodel'),
        ),
        migrations.AlterUniqueTogether(
            name='exchangerate',
            unique_together={('currency', 'base_currency')},
        ),
    ]
