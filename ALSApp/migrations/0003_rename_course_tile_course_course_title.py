# Generated by Django 5.0.4 on 2024-04-21 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ALSApp', '0002_course_alter_authapimodel_invitation_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_tile',
            new_name='course_title',
        ),
    ]
