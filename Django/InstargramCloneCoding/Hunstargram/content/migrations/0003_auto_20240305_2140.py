# Generated by Django 3.2.23 on 2024-03-05 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_remove_feed_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='user_name',
        ),
        migrations.AddField(
            model_name='feed',
            name='email',
            field=models.EmailField(default=2, max_length=254),
            preserve_default=False,
        ),
    ]
