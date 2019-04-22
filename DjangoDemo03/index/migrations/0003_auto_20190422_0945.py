# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-22 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_author_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='book',
            name='publicate',
            field=models.DateField(null=True),
        ),
    ]
