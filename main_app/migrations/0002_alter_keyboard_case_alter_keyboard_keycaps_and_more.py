# Generated by Django 4.0.4 on 2022-05-14 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyboard',
            name='case',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='keyboard',
            name='keycaps',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='keyboard',
            name='plate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='keyboard',
            name='stabilizers',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='keyboard',
            name='switches',
            field=models.CharField(max_length=100),
        ),
    ]
