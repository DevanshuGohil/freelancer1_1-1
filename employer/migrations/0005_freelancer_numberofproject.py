# Generated by Django 2.1.5 on 2019-03-02 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0004_project_finalselection'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='numberOfProject',
            field=models.IntegerField(default=0),
        ),
    ]
