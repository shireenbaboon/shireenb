# Generated by Django 2.2 on 2021-10-19 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managements', '0050_auto_20211013_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurses',
            name='doctor',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='managements.Doctors'),
        ),
    ]
