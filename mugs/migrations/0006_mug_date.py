# Generated by Django 3.1.3 on 2020-11-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mugs', '0005_remove_mug_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='mug',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
