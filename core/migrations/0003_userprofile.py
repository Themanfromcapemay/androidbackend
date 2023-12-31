# Generated by Django 4.2 on 2023-04-15 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_planet_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orion_credits', models.PositiveIntegerField(default=0)),
                ('population', models.PositiveIntegerField(default=0)),
                ('attack_points', models.PositiveIntegerField(default=0)),
                ('defense_points', models.PositiveIntegerField(default=0)),
                ('raiding_points', models.PositiveIntegerField(default=0)),
                ('player_class_choices', models.JSONField(default=dict)),
                ('player_class', models.CharField(blank=True, default='class1', max_length=50, null=True)),
                ('special_troops', models.JSONField(default=dict)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
