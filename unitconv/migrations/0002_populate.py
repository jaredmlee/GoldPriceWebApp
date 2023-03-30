# Generated by Django 4.1.6 on 2023-03-17 00:54

from django.db import migrations


def populate_db(apps, schema_editor):
    Units = apps.get_model('unitconv', 'Operator')

    units = Units(tonsToTroy=29166.7,
                  gramsToTroy=0.0321507,
                  troyToTroy=1,
                  kiloToTroy=32.1507,
                  poundToTroy=14.5833,
                  ounceToTroy=0.91146)

    units.save()


class Migration(migrations.Migration):
    dependencies = [
        ('unitconv', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db)
    ]
