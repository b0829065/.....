# Generated by Django 3.2.4 on 2021-06-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0011_auto_20210623_0106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='content',
            new_name='nickname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Stock_code',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='user_login',
            old_name='content',
            new_name='nickname',
        ),
        migrations.RenameField(
            model_name='user_login',
            old_name='Stock_code',
            new_name='password',
        ),
        migrations.AddField(
            model_name='user_login',
            name='login_check',
            field=models.BooleanField(default=False),
        ),
    ]
