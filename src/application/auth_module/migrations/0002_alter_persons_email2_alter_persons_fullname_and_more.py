# Generated by Django 4.1.2 on 2024-03-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='email2',
            field=models.EmailField(blank=True, default='', max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='persons',
            name='fullname',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='persons',
            name='phone',
            field=models.CharField(default='', max_length=50),
        ),
    ]
