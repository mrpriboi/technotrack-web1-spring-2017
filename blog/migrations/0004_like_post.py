# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170327_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
            preserve_default=False,
        ),
    ]