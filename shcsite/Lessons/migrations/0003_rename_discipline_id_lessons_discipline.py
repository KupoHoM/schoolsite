# Generated by Django 4.1.4 on 2023-02-06 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lessons', '0002_alter_lessons_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lessons',
            old_name='discipline_id',
            new_name='discipline',
        ),
    ]