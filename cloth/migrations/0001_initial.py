# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-30 20:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('types', models.CharField(choices=[('1', 'Accessories'), ('2', 'Dresses'), ('3', 'Jacket'), ('4', 'Pullovers'), ('5', 'T-Shirt'), ('6', 'Shirt'), ('7', 'Night Wear'), ('8', 'Jeans')], max_length=1)),
                ('url', models.TextField(default='', max_length=1024)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_clothes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
