# Generated by Django 3.2.7 on 2021-09-10 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_rename_school_campus_listing_campus_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='blog_number',
            new_name='block_number',
        ),
    ]
