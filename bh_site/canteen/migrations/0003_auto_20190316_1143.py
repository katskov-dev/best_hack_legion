# Generated by Django 2.0 on 2019-03-16 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0002_auto_20190316_1136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='canteenmodel',
            options={'permissions': (('edit_canteen', 'Edit Canteen'),), 'verbose_name': 'Столовая'},
        ),
    ]
