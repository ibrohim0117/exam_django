# Generated by Django 4.2.3 on 2023-07-26 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_alter_user_city_alter_user_job_alter_user_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_me',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
