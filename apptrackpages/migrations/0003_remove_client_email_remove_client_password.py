# Generated by Django 4.1.2 on 2022-12-09 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptrackpages', '0002_rename_testdummy_client_alter_client_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
        migrations.RemoveField(
            model_name='client',
            name='password',
        ),
    ]
