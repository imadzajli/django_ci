# Generated by Django 4.2.2 on 2024-08-26 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
