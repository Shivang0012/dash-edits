# Generated by Django 5.0.7 on 2024-09-16 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('clientid', models.AutoField(primary_key=True, serialize=False)),
                ('clientname', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=150)),
                ('rdate', models.CharField(max_length=150)),
                ('inventry', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='')),
                ('issue', models.TextField(max_length=5000)),
                ('cnotes', models.TextField(max_length=5000)),
                ('technician', models.CharField(max_length=150)),
                ('ddate', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
