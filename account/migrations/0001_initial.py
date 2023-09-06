# Generated by Django 4.2.3 on 2023-09-06 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('street_name', models.CharField(max_length=30)),
                ('street_number', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
