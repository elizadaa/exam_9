# Generated by Django 2.2 on 2019-04-06 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20190406_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='receipt_date',
            new_name='date',
        ),
    ]
