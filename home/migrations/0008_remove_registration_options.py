# Generated by Django 5.0.3 on 2024-04-29 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_alumni_id_remove_registration_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='Options',
        ),
    ]