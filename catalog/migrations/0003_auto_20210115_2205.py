# Generated by Django 3.1.5 on 2021-01-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210115_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='day_off1',
            field=models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='day_off2',
            field=models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], max_length=20),
        ),
    ]
