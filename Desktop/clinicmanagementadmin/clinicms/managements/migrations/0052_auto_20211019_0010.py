# Generated by Django 2.2 on 2021-10-19 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managements', '0051_auto_20211019_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurses',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'male'), ('F', 'female'), ('O', 'other')], default='M', max_length=1),
        ),
    ]
