# Generated by Django 3.2.7 on 2021-09-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_remove_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='miraboh', max_length=200),
            preserve_default=False,
        ),
    ]