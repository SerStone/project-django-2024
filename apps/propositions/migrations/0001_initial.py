# Generated by Django 5.0.6 on 2024-07-07 20:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PropositionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.CharField(max_length=100)),
                ('message', models.TextField(default='Your request is being processed.')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_reviewed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propositions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'propositions',
                'ordering': ['-id'],
            },
        ),
    ]
