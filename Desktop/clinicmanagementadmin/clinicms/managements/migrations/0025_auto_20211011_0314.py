# Generated by Django 2.2 on 2021-10-11 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managements', '0024_auto_20211011_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurses',
            name='gender',
            field=models.CharField(choices=[('M', 'male'), ('F', 'female'), ('O', 'other')], default=1, max_length=1),
        ),
    ]