# Generated by Django 4.2.2 on 2023-06-30 03:27

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
