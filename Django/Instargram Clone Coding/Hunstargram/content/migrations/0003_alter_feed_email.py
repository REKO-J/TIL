# Generated by Django 3.2.23 on 2024-02-04 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20240204_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]