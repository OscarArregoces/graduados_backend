# Generated by Django 4.1.2 on 2024-02-08 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0006_alter_eventos_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='fecha',
            field=models.DateField(default=datetime.date(2024, 2, 8)),
        ),
    ]
