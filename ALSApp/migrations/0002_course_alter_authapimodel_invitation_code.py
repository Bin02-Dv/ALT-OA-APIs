# Generated by Django 5.0.4 on 2024-04-21 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ALSApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor', models.EmailField(max_length=225, unique=True)),
                ('instructor_full_name', models.CharField(max_length=225)),
                ('course_tile', models.CharField(max_length=225)),
                ('course_slide', models.FileField(upload_to='course-slides')),
                ('course_video', models.FileField(upload_to='course-videos')),
            ],
        ),
        migrations.AlterField(
            model_name='authapimodel',
            name='invitation_code',
            field=models.CharField(blank=True, max_length=225),
        ),
    ]