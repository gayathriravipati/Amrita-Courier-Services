# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 12:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('StudentLogin', '0003_student_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_details',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
