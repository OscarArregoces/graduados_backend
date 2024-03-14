resources = [
    {
        "id_padre": 0,
        "path": "/inicio/",
        "icono": "pi pi-home",
        "method": "GET",
        "link": "/inicio/",
        "titulo": "Inicio",   #ID 1
        "items": [
            {
                "path": "/inicio/datos-personales/",
                "icono": "icon",
                "link": "/inicio/datos-personales/",
                "method": "GET",
                "titulo": "Datos Personales",   #ID 2
                "items": [
                    {
                        "path": "/inicio/datos-personales/actualizar-datos/",
                        "icono": "icon",
                        "method": "POST",
                        "link": "/inicio/datos-personales/actualizar-datos/",
                        "titulo": "Actualizar Datos",   #ID 3
                    },
                    {
                        "path": "/inicio/datos-personales/actualizar-datos/",
                        "icono": "icon",
                        "method": "POST",
                        "link": "/inicio/datos-personales/actualizar-datos/",
                        "titulo": "Actualizar Datos",   #ID 3
                    },
                ],
            },
        ],
    },
    {
        "path": "/admin/",
        "method": "GET",
        "id_padre": 0,
        "icono": "pi pi-th-large",
        "link": "/admin/",
        "titulo": "Administrador",   #ID 4
        "items": [
            {
                "path": "/admin/roles/",
                "method": "GET",
                "icono": "pi pi-th-large",
                "link": "/admin/roles/",
                "titulo": "Roles",    #ID 5
                "items": [
                    {
                        "path": "/admin/roles/usuarios/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/admin/roles/usuarios/",
                        "titulo": "Administrativos",    #ID 6
                    },
                    {
                        "path": "/admin/roles/permisos/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/admin/roles/permisos/",
                        "titulo": "Permisos",    #ID 7
                    },
                    {
                        "path": "/admin/roles/recursos/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/admin/roles/recursos/",
                        "titulo": "Recursos",    #ID 8
                    },
                ],
            },
            {
                "path": "/admin/usuarios/",
                "method": "GET",
                "icono": "pi pi-user-minus",
                "link": "/admin/usuarios/",
                "titulo": "Graduados",    #ID 9
                "items": [
                    {
                        "path": "/admin/usuarios/gestionar/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/admin/usuarios/gestionar/",
                        "titulo": "Gestionar",    #ID 10
                    }
                ],
            },
            {
                "path": "/admin/genero/",
                "method": "GET",
                "icono": "pi pi-user-minus",
                "link": "/admin/genero/",
                "titulo": "Generos",    #ID 11
                "items": [
                    {
                        "path": "/admin/gemero/gestionar/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/admin/genero/gestionar/",
                        "titulo": "Gestionar",    #ID 12
                    }
                ],
            },
            {
                "path": "/admin/tipo-identificacion/",
                "method": "GET",
                "icono": "pi pi-user-minus",
                "link": "/admin/tipo-identificacion/",
                "titulo": "T. Identificacion",    #ID 13
                "items": [
                    {
                        "path": "/admin/tipo-identificacion/gestionar/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/admin/tipo-identificacion/gestionar/",
                        "titulo": "Gestionar",    #ID 14
                    }
                ],
            },
            {
                "path": "/admin/reportes/",
                "method": "GET",
                "icono": "pi pi-user-minus",
                "link": "/admin/reportes/",
                "titulo": "Reportes",    #ID 15
                "items": [
                    {
                        "path": "/admin/reportes/ver/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/admin/reportes/ver/",
                        "titulo": "Gestionar",    #ID 16
                    }
                ],
            },
        ],
    },
    {
        "path": "/encuestas/",
        "id_padre": 0,
        "method": "GET",
        "icono": "pi pi-book",
        "link": "/encuestas/",
        "titulo": "Encuestas",   #ID 17
        "items": [
            {
                "path": "/encuestas/preguntas/",
                "method": "GET",
                "icono": "icon",
                "link": "/encuestas/preguntas/",
                "titulo": "Preguntas",   #ID 18
                "items": [
                    {
                        "path": "/encuestas/preguntas/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/encuestas/preguntas/gestionar/",
                        "titulo": "Gestionar",   #ID 19
                    }
                ],
            },
            {
                "path": "/encuestas/momentos/",
                "method": "GET",
                "icono": "icon",
                "link": "/encuestas/momentos/",
                "titulo": "Momentos",   #ID 20
                "items": [
                    {
                        "path": "/encuestas/momentos/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/encuestas/momentos/gestionar/",
                        "titulo": "Gestionar",   #ID 21
                    }
                ],
            },
            {
                "path": "/encuestas/mis-encuestas/",
                "method": "GET",
                "icono": "icon",
                "link": "/encuestas/mis-encuestas/",
                "titulo": "Encuestas",   #ID 22
                "items": [
                    {
                        "path": "/encuestas/mis-encuestas/llenar-encuestas/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/encuestas/mis-encuestas/llenar-encuestas/",
                        "titulo": "Mis Encuestas",   #ID 23
                    }
                ],
            },
        ],
    },
    {
        "path": "/pqrs/",
        "id_padre": 0,
        "method": "GET",
        "icono": "pi pi-folder",
        "link": "/pqrs/",
        "titulo": "PQRS",   #ID 24
        "items": [
            {
                "path": "/pqrs/solicitud/",
                "method": "GET",
                "icono": "icon",
                "link": "/pqrs/solicitud/",
                "titulo": "Solicitud",   #ID 25
                "items": [
                    {
                        "path": "/pqrs/solicitud/crear/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/crear/",
                        "titulo": "Generar",    #ID 26
                    },
                    {
                        "path": "/pqrs/solicitud/ver/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/ver/",
                        "titulo": "Ver",    #ID 27
                    },
                    {
                        "path": "/pqrs/solicitud/editar/",
                        "method": "PUT",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/editar/",
                        "titulo": "Actualizar",    #ID 28
                    },
                    {
                        "path": "/pqrs/solicitud/eliminar/",
                        "method": "DELETE",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/eliminar/",
                        "titulo": "Eliminar",    #ID 29
                    },
                    {
                        "path": "/pqrs/solicitud/mis-solicitudes/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/mis-solicitudes/",
                        "titulo": "Mis Solicitudes",    #ID 30
                    },
                ],
            },
            {
                "path": "/pqrs/tipo/",
                "method": "GET",
                "icono": "icon",
                "link": "/pqrs/tipo/",
                "titulo": "Tipo de Solicitud",   #ID 31
                "items": [
                    {
                        "path": "/pqrs/tipo/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/pqrs/tipo/gestionar/",
                        "titulo": "Gestionar",   #ID 32
                    }
                ],
            },
            {
                "path": "/pqrs/asignacion/",
                "method": "GET",
                "icono": "icon",
                "link": "/pqrs/asignacion/",
                "titulo": "Asignación",   #ID 33
                "items": [
                    {
                        "path": "/pqrs/asignacion/mis-solicitudes",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/pqrs/asignacion/mis-solicitudes",
                        "titulo": "Mis Solicitudes",    #ID 34
                    },
                    {
                        "path": "/pqrs/asignacion/solicitudes",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/pqrs/asignacion/solicitudes",
                        "titulo": "Solicitudes",    #ID 35
                    },
                ],
            },
        ],
    },
    {
        "path": "/clasificados/",
        "id_padre": 0,
        "method": "GET",
        "icono": "pi pi-briefcase",
        "link": "/clasificados/",
        "titulo": "Clasificados",   #ID 36
        "items": [
            {
                "path": "/clasificados/emprendimientos/",
                "method": "GET",
                "icono": "icon",
                "link": "/clasificados/emprendimientos/",
                "titulo": "Emprendimientos",    #ID 37
                "items": [
                    {
                        "path": "/clasificados/emprendimientos/crear/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/crear/",
                        "titulo": "Crear",    #ID 38
                    },
                    {
                        "path": "/clasificados/emprendimientos/ver/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/ver/",
                        "titulo": "Ver",    #ID 39
                    },
                    {
                        "path": "/clasificados/emprendimientos/editar/",
                        "method": "PUT",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/editar/",
                        "titulo": "Editar",    #ID 40
                    },
                    {
                        "path": "/clasificados/emprendimientos/eliminar/",
                        "method": "DELETE",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/eliminar/",
                        "titulo": "Eliminar",    #ID 41
                    },
                    {
                        "path": "/clasificados/emprendimientos/mis-emprendimientos/",
                        "method": "DELETE",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/mis-emprendimientos/",
                        "titulo": "Mis Emprendimientos",    #ID 42
                    },
                    {
                        "path": "/clasificados/emprendimientos/detalles/",
                        "method": "DELETE",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/detalles/",
                        "titulo": "Detalles",    #ID 43
                    },
                ],
            },
            {
                "path": "/clasificados/categoria/",
                "method": "GET",
                "icono": "icon",
                "link": "/clasificados/categoria/",
                "titulo": "Categorias",    #ID 44
                "items": [
                    {
                        "path": "/clasificados/categoria/gestionar",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/clasificados/categoria/gestionar",
                        "titulo": "Gestionar",    #ID 45
                    }
                ],
            },
            {
                "path": "/clasificados/sub-categoria/",
                "method": "GET",
                "icono": "icon",
                "link": "/clasificados/sub-categoria/",
                "titulo": "Subcategorias",    #ID 46
                "items": [
                    {
                        "path": "/clasificados/sub-categoria/gestionar",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/clasificados/sub-categoria/gestionar",
                        "titulo": "Gestionar",    #ID 47
                    }
                ],
            },
            {
                "path": "/clasificados/capacitaciones/",
                "method": "GET",
                "icono": "icon",
                "link": "/clasificados/capacitaciones/",
                "titulo": "Capacitaciones",    #ID 48
                "items": [
                    {
                        "path": "/clasificados/capacitaciones/gestionar",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/clasificados/capacitaciones/gestionar",
                        "titulo": "Gestionar",    #ID 49
                    }
                ],
            },
        ],
    },
    {
        "path": "/eventos/",
        "id_padre": 0,
        "method": "GET",
        "icono": "pi pi-ticket",
        "link": "/eventos/",
        "titulo": "Eventos",    #ID 50
        "items": [
            {
                "path": "/eventos/actividades/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/actividades/",
                "titulo": "Actividades",    #ID 51
                "items": [
                    {
                        "path": "/eventos/actividades/crear/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/eventos/actividades/crear/",
                        "titulo": "Solicitar",    #ID 52
                    },
                    {
                        "path": "/eventos/actividades/aprobacion/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/actividades/aprobacion/",
                        "titulo": "Aprobación",    #ID 53
                    },
                    {
                        "path": "/eventos/actividades/ver/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/actividades/ver/",
                        "titulo": "Reportes",    #ID 54
                    },
            
                    {
                        "path": "/eventos/actividades/editar/",
                        "method": "PUT",
                        "icono": "icon",
                        "link": "/eventos/actividades/editar/",
                        "titulo": "Actualizar",    #ID 55
                    },
                    {
                        "path": "/eventos/actividades/eliminar/",
                        "method": "DELETE",
                        "icono": "icon",
                        "link": "/eventos/actividades/eliminar/",
                        "titulo": "Eliminar",    #ID 56
                    },
                    {
                        "path": "/eventos/actividades/mis-actividades/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/actividades/mis-actividades/",
                        "titulo": "Mis Actividades",    #ID 57
                    },
                    {
                        "path": "/eventos/actividades/asistencias/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/actividades/asistencias/",
                        "titulo": "Asistencias",    #ID 58
                    },
                ],
            },
            {
                "path": "/eventos/areas/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/areas/",
                "titulo": "Areas",    #ID 59
                "items": [
                    {
                        "path": "/eventos/areas/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/areas/gestionar/",
                        "titulo": "Gestionar",    #ID 60
                    }
                ],
            },
            {
                "path": "/eventos/subareas/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/subareas/",
                "titulo": "Subareas",    #ID 61
                "items": [
                    {
                        "path": "/eventos/subareas/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/subareas/gestionar/",
                        "titulo": "Gestionar",    #ID 62
                    }
                ],
            },
            {
                "path": "/eventos/tipo-actividad/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/tipo-actividad/",
                "titulo": "Tipo Actividad",    #ID 63
                "items": [
                    {
                        "path": "/eventos/tipo-actividad/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/tipo-actividad/gestionar/",
                        "titulo": "Gestionar",    #ID 64
                    }
                ],
            },
            {
                "path": "/eventos/programa/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/programa/",
                "titulo": "Programas",    #ID 65
                "items": [
                    {
                        "path": "/eventos/programa/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/programa/gestionar/",
                        "titulo": "Gestionar",    #ID 66
                    }
                ],
            },
            {
                "path": "/eventos/sede/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/sede/",
                "titulo": "Sedes",    #ID 67
                "items": [
                    {
                        "path": "/eventos/sede/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/sede/gestionar/",
                        "titulo": "Gestionar",    #ID 68
                    }
                ],
            },
            {
                "path": "/eventos/facultad/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/facultad/",
                "titulo": "Facultades",    #ID 69
                "items": [
                    {
                        "path": "/eventos/facultad/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/facultad/gestionar/",
                        "titulo": "Gestionar",    #ID 70
                    }
                ],
            },
            # {
            #     "path": "/eventos/asistencias/",
            #     "method": "GET",
            #     "icono": "icon",
            #     "link": "/eventos/asistencias/",
            #     "titulo": "Asistencias",
            #     "items": [
            #         {
            #             "path": "/eventos/asistencias/ver-asistencias/",
            #             "method": "GET",
            #             "icono": "icon",
            #             "link": "/eventos/asistencias/ver-asistencias/",
            #             "titulo": "Ver Asistencias",
            #         },
            #         {
            #             "path": "/eventos/asistencias/llenar-asistencias/",
            #             "method": "GET",
            #             "icono": "icon",
            #             "link": "/eventos/asistencias/llenar-asistencias/",
            #             "titulo": "LLenar Asistencias",
            #         },
            #     ],
            # },
        ],
    },
]

resources_graduados = [
{"id":1},
{"id":2},
{"id":3},
{"id":17},
{"id":22},
{"id":23},
{"id":24},
{"id":25},
{"id":26},
{"id":30},
{"id":36},
{"id":37},
{"id":38},
{"id":42},
{"id":43},
{"id":50},
{"id":51},
{"id":57},
]
resources_funcionario = [
    {"id":1},
    {"id":2},
    {"id":3},
    {"id":4},
    {"id":5},
    {"id":6},
    {"id":7},
    {"id":8},
    {"id":9},
    {"id":10},
    {"id":15},
    {"id":16},
    {"id":24},
    {"id":25},
    {"id":27},
    {"id":33},
    {"id":34},
    {"id":35},
    {"id":50},
    {"id":51},
    {"id":52},
    {"id":53},
    {"id":54},
    {"id":58},
]