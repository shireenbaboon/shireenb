# Generated by Django 2.2 on 2021-10-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managements', '0010_patients_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctors',
            options={'verbose_name_plural': 'Doctors'},
        ),
        migrations.AlterField(
            model_name='doctors',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default=3),
        ),
        migrations.AlterField(
            model_name='nurses',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default=3),
        ),
        migrations.AlterField(
            model_name='patients',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default=3),
        ),
    ]