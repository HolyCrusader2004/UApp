# Generated by Django 5.1.4 on 2024-12-26 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_func', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingslots',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('occupied', 'Occupied')], default='Available', max_length=90),
        ),
    ]
