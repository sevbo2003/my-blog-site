# Generated by Django 4.0.2 on 2022-02-17 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={},
        ),
        migrations.RemoveField(
            model_name='email',
            name='created_at',
        ),
    ]
