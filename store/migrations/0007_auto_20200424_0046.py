# Generated by Django 2.2.3 on 2020-04-23 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200424_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='Gift_type',
            field=models.CharField(max_length=30),
        ),
    ]
