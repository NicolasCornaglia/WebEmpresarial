# Generated by Django 5.0.6 on 2024-08-01 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_publichsed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publichsed',
            new_name='published',
        ),
    ]
