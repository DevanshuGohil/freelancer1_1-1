# Generated by Django 2.1.5 on 2019-03-14 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0010_chat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='message',
            new_name='messageReq',
        ),
        migrations.AddField(
            model_name='chat',
            name='messageRes',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
