# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-15 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_book_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='approve_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
