# Generated by Django 3.1.1 on 2020-09-22 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpeedTestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('ping', models.FloatField(null=True)),
                ('download', models.FloatField(null=True)),
                ('upload', models.FloatField(null=True)),
                ('json', models.JSONField()),
            ],
        ),
    ]
