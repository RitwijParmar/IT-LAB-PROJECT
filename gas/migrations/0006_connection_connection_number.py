# Generated by Django 3.1 on 2020-09-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas', '0005_auto_20200917_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='connection_Number',
            field=models.CharField(blank=True, default='8431679283', editable=False, max_length=10, unique=True),
        ),
    ]