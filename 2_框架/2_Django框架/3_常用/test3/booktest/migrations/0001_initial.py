# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('atitle', models.CharField(max_length=30)),
                ('aParent', models.ForeignKey(null=True, to='booktest.AreaInfo', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PicTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('pic', models.ImageField(upload_to='booktest/')),
            ],
        ),
    ]
