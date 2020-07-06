# Generated by Django 2.2.3 on 2019-08-14 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=30)),
                ('c_email', models.EmailField(max_length=254)),
                ('c_phno', models.IntegerField(max_length=10)),
                ('c_address', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=30)),
                ('e_sal', models.CharField(max_length=50)),
                ('e_designation', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=30)),
                ('g_gifttype', models.CharField(max_length=50)),
                ('g_costprice', models.CharField(max_length=60)),
                ('headshot', models.ImageField(upload_to='store/static/img')),
            ],
        ),
        migrations.CreateModel(
            name='gift_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_type', models.CharField(max_length=10)),
                ('g_description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=30)),
                ('c_email', models.EmailField(max_length=254)),
                ('c_phno', models.IntegerField(max_length=10)),
                ('c_address', models.CharField(max_length=30)),
                ('t_paymode', models.CharField(max_length=50)),
                ('t_amount', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_gift', models.CharField(max_length=30)),
                ('t_paymode', models.CharField(max_length=50)),
                ('t_amount', models.IntegerField(max_length=10)),
                ('t_paytime', models.DateTimeField()),
            ],
        ),
    ]