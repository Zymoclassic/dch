# Generated by Django 5.0.1 on 2024-02-09 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('maker', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('mileage', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
