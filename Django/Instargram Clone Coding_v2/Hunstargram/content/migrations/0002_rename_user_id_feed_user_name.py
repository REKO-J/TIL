# Generated by Django 3.2.23 on 2024-02-08 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='user_id',
            new_name='user_name',
        ),
    ]
