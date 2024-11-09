# Generated by Django 5.0.5 on 2024-10-23 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_management', '0003_alter_collegeprogram_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collegeprogram',
            name='enrollment_term',
            field=models.CharField(choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Fall', 'Fall'), ('Winter', 'Winter')], default='Spring', max_length=20),
        ),
    ]
