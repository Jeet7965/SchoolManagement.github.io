# Generated by Django 3.2.9 on 2023-01-10 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schl_mng_app', '0015_auto_20230108_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_notification',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]