# Generated by Django 2.2 on 2021-10-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20211007_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Doctor'), (2, 'Nurses'), (3, 'Management')], default=2),
        ),
    ]
