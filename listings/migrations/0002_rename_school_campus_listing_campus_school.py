# Generated by Django 3.2.7 on 2021-09-10 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='school_campus',
            new_name='campus_school',
        ),
    ]
