# Generated by Django 4.1.5 on 2023-02-11 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_job_post_is_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='fk',
            new_name='owner',
        ),
    ]
