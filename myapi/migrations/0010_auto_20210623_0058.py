# Generated by Django 3.2.4 on 2021-06-22 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0009_auto_20210623_0026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='nickname',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='user_login',
            old_name='nickname',
            new_name='content',
        ),
    ]