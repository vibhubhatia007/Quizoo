# Generated by Django 3.1.1 on 2020-10-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizer', '0017_testlogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testlogs',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
