# Generated by Django 2.0.5 on 2018-06-12 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miscelanea', '0002_auto_20180608_1546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noinclude',
            options={'ordering': ['-created'], 'verbose_name': 'No Incluye', 'verbose_name_plural': 'No Incluye'},
        ),
    ]
