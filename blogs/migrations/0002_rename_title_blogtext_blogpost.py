# Generated by Django 5.0.3 on 2024-03-18 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogtext',
            old_name='title',
            new_name='blogpost',
        ),
    ]