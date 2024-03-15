# Generated by Django 4.1.2 on 2024-03-15 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import src.validators.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
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
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='TiposCapacitaciones',
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
                'verbose_name': 'Capacitacion',
                'verbose_name_plural': 'Capacitacitaciones',
            },
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('createdAt', models.DateField(auto_now_add=True, null=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('categoriaId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_id', to='classified_advertisements.categoria')),
                ('userCreate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('userUpdate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'SubCategoria',
                'verbose_name_plural': 'SubCategorias',
            },
        ),
        migrations.CreateModel(
            name='RedesSociales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('createdAt', models.DateField(auto_now_add=True, null=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('link', models.CharField(max_length=500)),
                ('userCreate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('userUpdate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('createdAt', models.DateField(auto_now_add=True, null=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('mensaje', models.CharField(default='', max_length=500)),
                ('userCreate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('userUpdate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
            },
        ),
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('createdAt', models.DateField(auto_now_add=True, null=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('nombre_emprendimiento', models.CharField(max_length=256)),
                ('descripcion', models.CharField(max_length=600)),
                ('telefono_emprendimiento', models.CharField(max_length=11)),
                ('correo_emprendimiento', models.EmailField(max_length=254)),
                ('corregimiento', models.CharField(blank=True, max_length=50, null=True)),
                ('municipio', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion', models.CharField(max_length=50)),
                ('metodos_entrega', models.CharField(max_length=900)),
                ('formas_pago', models.CharField(max_length=900)),
                ('logo', models.FileField(blank=True, null=True, upload_to='eventos/%Y/', validators=[src.validators.index.validate_image, src.validators.index.extension_type])),
                ('state', models.BooleanField(default=False)),
                ('state_value', models.CharField(default='Pendiente', max_length=50)),
                ('mensajes', models.ManyToManyField(null=True, to='classified_advertisements.mensajes')),
                ('redes', models.ManyToManyField(db_index=True, related_name='redes_store', to='classified_advertisements.redessociales')),
                ('subCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classified_advertisements.subcategoria')),
                ('tipo_capacitacion', models.ManyToManyField(db_index=True, to='classified_advertisements.tiposcapacitaciones')),
                ('userCreate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('userUpdate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Anuncio',
                'verbose_name_plural': 'Anuncios',
            },
            managers=[
                ('objects_subCategory', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='VotoAnuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emprendimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classified_advertisements.anuncio')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('emprendimiento', 'user')},
            },
        ),
    ]
