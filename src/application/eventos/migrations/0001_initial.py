# Generated by Django 4.1.2 on 2024-02-29 16:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventosArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('createdAt', models.DateField(auto_now_add=True, null=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('userCreate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('userUpdate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Area Evento',
                'verbose_name_plural': 'Areas Eventos',
            },
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('createdAt', models.DateField(auto_now_add=True, null=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('userCreate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('userUpdate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tipo Evento',
                'verbose_name_plural': 'Tipo Eventos',
            },
        ),
        migrations.CreateModel(
            name='SubAreaEventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('createdAt', models.DateField(auto_now_add=True, null=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='eventos.eventosarea')),
                ('userCreate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('userUpdate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sub Area Evento',
                'verbose_name_plural': 'Sub Areas Eventos',
            },
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('createdAt', models.DateField(auto_now_add=True, null=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('nombre_actividad', models.CharField(max_length=256)),
                ('tipo_actividad', models.CharField(max_length=256)),
                ('responsable', models.CharField(max_length=256)),
                ('fecha', models.DateField(default=datetime.date(2024, 2, 29))),
                ('hora', models.CharField(max_length=10)),
                ('lugar', models.CharField(max_length=256)),
                ('cupos', models.IntegerField()),
                ('descripcion', models.CharField(max_length=600)),
                ('objectivo', models.CharField(max_length=300)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='eventos.eventosarea')),
                ('dirigido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_module.programs')),
                ('subArea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='eventos.subareaeventos')),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.tipoevento')),
                ('userCreate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('userUpdate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.eventos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('evento', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('createdAt', models.DateField(auto_now_add=True, null=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('confirm', models.BooleanField(default=False)),
                ('asistencia', models.BooleanField(default=False)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.eventos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('userCreate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('userUpdate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('evento', 'user')},
            },
        ),
    ]
