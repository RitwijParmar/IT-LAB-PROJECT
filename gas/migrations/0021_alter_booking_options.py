# Generated by Django 3.2.16 on 2022-12-01 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gas', '0020_auto_20201005_2151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'permissions': (('can_change_status', 'Can Change Status'),)},
        ),
    ]