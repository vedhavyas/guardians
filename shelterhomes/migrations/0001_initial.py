# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 11:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShelterHome',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Name of the Shelter Home.', max_length=50, unique=True)),
                ('phone', models.CharField(blank=True, help_text='Primary contact number.', max_length=20, null=True)),
                ('contact_name', models.CharField(blank=True, help_text='Primary contact name', max_length=30, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShelterHomeDetails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('alternate_phone', models.CharField(blank=True, help_text='Alternate contact number', max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('org_type', models.PositiveSmallIntegerField(choices=[(1, 'Trust'), (2, 'Society'), (3, 'Other')], default=3)),
                ('years_of_operation', models.PositiveIntegerField(blank=True, null=True)),
                ('home_type', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Boys'), (2, 'Girls'), (3, 'Boys & Girls')], null=True)),
                ('total_children', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Shelter Home Details',
                'verbose_name_plural': 'Shelter Homes Details',
            },
        ),
        migrations.AddField(
            model_name='shelterhome',
            name='details',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shelterhomes.ShelterHomeDetails'),
        ),
    ]
