# Generated by Django 5.0.3 on 2024-04-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alumni_registration_volunteer_delete_alumniss_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumni',
            name='id',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='id',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='id',
        ),
        migrations.AddField(
            model_name='alumni',
            name='a_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='r_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='v_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
