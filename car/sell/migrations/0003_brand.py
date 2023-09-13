# Generated by Django 4.2.5 on 2023-09-13 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0002_car_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Brand')),
                ('image', models.ImageField(upload_to='carbrands')),
            ],
        ),
    ]
