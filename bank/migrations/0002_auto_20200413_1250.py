# Generated by Django 3.0.5 on 2020-04-13 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Banks',
            new_name='Bank',
        ),
        migrations.RenameModel(
            old_name='Branches',
            new_name='Branch',
        ),
    ]
