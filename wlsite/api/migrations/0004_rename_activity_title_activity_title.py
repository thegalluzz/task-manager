# Generated by Django 3.2.9 on 2022-03-08 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_activity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='activity_title',
            new_name='title',
        ),
    ]
