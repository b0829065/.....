# Generated by Django 3.2.4 on 2021-06-22 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0012_auto_20210623_0154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_login',
            name='login_check',
        ),
    ]