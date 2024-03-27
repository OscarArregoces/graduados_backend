from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from configs.seeds.GraduadosSeed import GraduadosSeed
from configs.seeds.UniversidadSeed import SedesSeed
import src.validators.index
import re
from configs.helpers.menu import resources as menu_resources, resources_graduados, resources_funcionario
from configs.helpers.menu_resources import menuResources
from django.contrib.auth.models import Group
from configs.seeds.EventosSeed import AreasActividadSeed, EventosStatusSeed, ServiciosSeed, SubareasActividadSeed, TipoActividadSeed
from configs.seeds.AuthSeed import CondicionesSeed, DocumentTypeSeed, GendersSeed, GestoresSeed, GroupsSeed, PersonsSeed, UsersSeed
from configs.seeds.ClasificadosSeed import CapacitacionesSeed, EmprendimientosSeed
from configs.seeds.PaisesSeed import CiudadesSeed, DepartamentosSeed, PaisesSeed



class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    
    def insert_init_data(apps, schema_editor):
        
        Paises = apps.get_model("auth_module", "Pais") # type: ignore
        Departamentos = apps.get_model("auth_module", "Departamento") # type: ignore
        Ciudades = apps.get_model("auth_module", "Ciudad") # type: ignore
        
        Paises.objects.bulk_create(
            [Paises(**data) for data in PaisesSeed]
        )
        Departamentos.objects.bulk_create(
            [Departamentos(**data) for data in DepartamentosSeed]
        )
        Ciudades.objects.bulk_create(
            [Ciudades(**data) for data in CiudadesSeed]
        )
        
        Sedes = apps.get_model("auth_module", "Headquarters") # type: ignore
        # Facultades = apps.get_model("auth_module", "Faculties") # type: ignore
        # Programas = apps.get_model("auth_module", "Programs") # type: ignore
        
        Sedes.objects.bulk_create(
            [Sedes(**data) for data in SedesSeed]
        )
        
        
        CondicionesVulnerables = apps.get_model("auth_module", "CondicionVulnerable") # type: ignore
        CondicionesVulnerables.objects.bulk_create(
            [CondicionesVulnerables(**data) for data in CondicionesSeed]
        )
        
        CategoriasEmprendimientos = apps.get_model("classified_advertisements", "Categoria") # type: ignore
        SubCategoriasEmprendimientos = apps.get_model("classified_advertisements", "SubCategoria") # type: ignore

        for categoria_name, subcategorias_list in EmprendimientosSeed:
            categoria = CategoriasEmprendimientos.objects.create(name=categoria_name)
            subcategorias = [
                SubCategoriasEmprendimientos(name=subcategoria, categoriaId_id=categoria.id)
                for subcategoria in subcategorias_list
            ]
            SubCategoriasEmprendimientos.objects.bulk_create(subcategorias)
        
        Capacitaciones = apps.get_model("classified_advertisements", "TiposCapacitaciones") # type: ignore
        Capacitaciones.objects.bulk_create(
            [Capacitaciones(**data) for data in CapacitacionesSeed]
        )
        
        TipoActividad = apps.get_model("eventos", "TipoEvento") # type: ignore
        TipoActividad.objects.bulk_create(
            [TipoActividad(**data) for data in TipoActividadSeed]
        )
        
        AreaEvento = apps.get_model("eventos", "EventosArea") # type: ignore
        SubareaEvento = apps.get_model("eventos", "SubAreaEventos") # type: ignore
        Servicios = apps.get_model("eventos", "Servicios") # type: ignore
        EventosStatus = apps.get_model("eventos", "EventosStatus") # type: ignore
        
        AreaEvento.objects.bulk_create([AreaEvento(**data) for data in AreasActividadSeed])
        SubareaEvento.objects.bulk_create([SubareaEvento(**data) for data in SubareasActividadSeed])
        Servicios.objects.bulk_create([Servicios(**data) for data in ServiciosSeed])
        EventosStatus.objects.bulk_create([EventosStatus(**data) for data in EventosStatusSeed])
        
        Gestor = apps.get_model("auth_module", "Gestor") # type: ignore
        Gestor.objects.bulk_create([Gestor(**data) for data in GestoresSeed])
 
        
        User = apps.get_model("auth_module", "User") # type: ignore
        Person = apps.get_model("auth_module", "Persons") # type: ignore
        Carrera = apps.get_model("auth_module", "Carrera") # type: ignore
        User_roles = apps.get_model("auth_module", "user_groups") # type: ignore
        User_documents = apps.get_model("auth_module", "document_types") # type: ignore
        User_genders = apps.get_model("auth_module", "genders") # type: ignore
       
        Group.objects.bulk_create([Group(**data) for data in GroupsSeed])

        User_documents.objects.bulk_create([User_documents(**data) for data in DocumentTypeSeed])

        User_genders.objects.bulk_create([User_genders(**data) for data in GendersSeed])

        Person.objects.bulk_create([Person(**data) for data in PersonsSeed])
        
        User.objects.bulk_create([User(**data) for data in UsersSeed])
        
        # CARGA DE GRADUADOS
        for graduado in GraduadosSeed:
            persona_data = graduado['persona']
            persona = Person.objects.create(**persona_data)

            user_data = graduado['user']
            user_data['person_id'] = persona.id  
            user = User.objects.create(**user_data)

            carreras_data = graduado['carreras']
            for carrera_data in carreras_data:
                carrera_data['person_id'] = persona.id 
                Carrera.objects.create(**carrera_data)
        
        user = User.objects.all()
        roles = Group.objects.all()
        list_user_roles = []
        for u in user:
            for r in roles:
                if u.username == "graduado" and r.name == "Graduado":
                    list_user_roles.append(
                        User_roles(user_id=u.id, group_id=r.id), # type: ignore
                    )
                elif u.username == "admin" and r.name == "Admin":
                    list_user_roles.append(
                        User_roles(user_id=u.id, group_id=r.id), # type: ignore
                    )
                elif u.username == "3333333333" and r.name == "Funcionario":
                    list_user_roles.append(
                        User_roles(user_id=u.id, group_id=r.id), # type: ignore
                    )
                elif u.username == "4444444444" and r.name == "Funcionario":
                    list_user_roles.append(
                        User_roles(user_id=u.id, group_id=r.id), # type: ignore
                    )

        User_roles.objects.bulk_create(list_user_roles)

        Resources = apps.get_model("auth_module", "Resources")  # type: ignore
        resources = []
        menuResources(menu_resources, resources, Resources, 1)

        resources = Resources.objects.bulk_create(resources)

        Resources_roles = apps.get_model("auth_module", "Resources_roles")  # type: ignore
        list_resources_roles = []
        roles = Group.objects.all()
        
        for rol in roles:
            if rol.name == "Graduado":
                for r in resources_graduados:
                    resource_instance = Resources.objects.get(id=r["id"])
                    list_resources_roles.append(Resources_roles(rolesId_id=rol.id, resourcesId=resource_instance))  # type: ignore
            if rol.name == "Funcionario":
                for r in resources_funcionario:
                    resource_instance = Resources.objects.get(id=r["id"])
                    list_resources_roles.append(Resources_roles(rolesId_id=rol.id, resourcesId=resource_instance))  # type: ignore
            if rol.name == "Admin":
                for r in resources:
                    list_resources_roles.append(
                        Resources_roles(rolesId_id=rol.id, resourcesId=r) # type: ignore
                    )

        Resources_roles.objects.bulk_create(list_resources_roles)

    def undo_insert_data(apps, schema_editor):
            Group.objects.all().delete()
            CondicionesVulnerables = apps.get_model("auth_module", "CondicionesVulnerables") # type: ignore
            CondicionesVulnerables.objects.all().delete()
            CategoriasEmprendimientos = apps.get_model("classified_advertisements", "Categoria") # type: ignore
            CategoriasEmprendimientos.objects.all().delete()
            SubCategoriasEmprendimientos = apps.get_model("classified_advertisements", "SubCategoria") # type: ignore
            SubCategoriasEmprendimientos.objects.all().delete()
            Capacitaciones = apps.get_model("classified_advertisements", "TiposCapacitaciones") # type: ignore
            Capacitaciones.objects.all().delete()
            TipoActividad = apps.get_model("eventos", "TipoEvento") # type: ignore
            TipoActividad.objects.all().delete()
            AreaEvento = apps.get_model("eventos", "EventosArea") # type: ignore
            AreaEvento.objects.all().delete()
            SubareaEvento = apps.get_model("eventos", "SubAreaEventos") # type: ignore
            SubareaEvento.objects.all().delete()
            Gestor = apps.get_model("auth_module", "Gestor") # type: ignore
            Gestor.objects.all().delete()
            User = apps.get_model("auth_module", "User") # type: ignore
            User.objects.all().delete()
            Person = apps.get_model("auth_module", "Persons") # type: ignore
            Person.objects.all().delete()
            User_roles = apps.get_model("auth_module", "user_groups") # type: ignore
            User_roles.objects.all().delete()
            User_documents = apps.get_model("auth_module", "document_types") # type: ignore
            User_documents.objects.all().delete()
            User_genders = apps.get_model("auth_module", "genders") # type: ignore
            User_genders.objects.all().delete()
            Carrera = apps.get_model("auth_module", "Carrera") # type: ignore
            Carrera.objects.all().delete()
            Resources = apps.get_model("auth_module", "Resources") # type: ignore
            Resources.objects.all().delete()
            Resources_roles = apps.get_model("auth_module", "Resources_roles") # type: ignore
            Resources_roles.objects.all().delete()
            Paises = apps.get_model("auth_module", "Pais") # type: ignore
            Paises.objects.all().delete()
            Departamentos = apps.get_model("auth_module", "Departamento") # type: ignore
            Departamentos.objects.all().delete()
            Ciudades = apps.get_model("auth_module", "Ciudad") # type: ignore
            Ciudades.objects.all().delete()
            Sedes = apps.get_model("auth_module", "Headquarters") # type: ignore
            Sedes.objects.all().delete()
            EventosStatus = apps.get_model("eventos", "EventosStatus") # type: ignore
            EventosStatus.objects.all().delete()
            Carrera = apps.get_model("auth_module", "Carrera") # type: ignore
            Carrera.objects.all().delete()
            
        

    operations = [
        migrations.CreateModel(
            name='Pqrs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('createdAt', models.DateField(auto_now_add=True, null=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('titulo', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=600)),
                ('anexo', models.FileField(blank=True, null=True, upload_to='pqrs/%Y/', validators=[src.validators.index.validate_image, src.validators.index.extension_type])),
                ('status', models.CharField(choices=[('FN', 'Finalizada'), ('AC', 'Activa'), ('EP', 'En espera')], default='AC', max_length=10)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pqrs',
            },
        ),
        migrations.CreateModel(
            name='TipoPqrs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('createdAt', models.DateField(auto_now_add=True, null=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('tipo', models.CharField(max_length=256)),
                ('userCreate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('userUpdate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('createdAt', models.DateField(auto_now_add=True, null=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('anexo', models.FileField(blank=True, null=True, upload_to='pqrs/%Y/respuesta/')),
                ('descripcion', models.CharField(blank=True, max_length=600, null=True)),
                ('pqrs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuesta_pqrs', to='pqrs.pqrs')),
                ('userCreate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('userUpdate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Respuesta',
                'verbose_name_plural': 'Respuestas',
            },
        ),
        migrations.AddField(
            model_name='pqrs',
            name='tipopqrs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pqrs.tipopqrs'),
        ),
        migrations.AddField(
            model_name='pqrs',
            name='userCreate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pqrs',
            name='userUpdate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('createdAt', models.DateField(auto_now_add=True, null=True)),
                ('updateAt', models.DateField(auto_now=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('fecha_asignacion', models.DateField(auto_now=True)),
                ('funcionarioId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pqrs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pqrs.pqrs')),
                ('userCreate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('userUpdate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Asignacion',
                'verbose_name_plural': 'Asignacions',
            },
        ),
         migrations.RunPython(
            insert_init_data, reverse_code=undo_insert_data, atomic=True
        ),
    ]
