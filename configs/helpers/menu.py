resources = [
    {
        "id_padre": 0,
        "path": "/inicio/",
        "icono": "pi pi-home",
        "method": "GET",
        "link": "/inicio/",
        "titulo": "Inicio",
        "items": [
            {
                "path": "/inicio/datos-personales/",
                "icono": "icon",
                "link": "/inicio/datos-personales/",
                "method": "GET",
                "titulo": "Datos Personales",
                "items": [
                    {
                        "path": "/inicio/datos-personales/actualizar-datos/",
                        "icono": "icon",
                        "method": "POST",
                        "link": "/inicio/datos-personales/actualizar-datos/",
                        "titulo": "Actualizar Datos",
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
        "titulo": "Admin",
        "items": [
            {
                "path": "/admin/roles/",
                "method": "GET",
                "icono": "pi pi-th-large",
                "link": "/admin/roles/",
                "titulo": "Roles",
                "items": [
                    {
                        "path": "/admin/roles/usuarios/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/admin/roles/usuarios/",
                        "titulo": "Usuarios",
                    },
                    {
                        "path": "/admin/roles/permisos/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/admin/roles/permisos/",
                        "titulo": "Permisos",
                    },
                    {
                        "path": "/admin/roles/recursos/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/admin/roles/recursos/",
                        "titulo": "Recursos",
                    },
                ],
            },
            {
                "path": "/admin/usuarios/",
                "method": "GET",
                "icono": "pi pi-user-minus",
                "link": "/admin/usuarios/",
                "titulo": "Usuarios",
                "items": [
                    {
                        "path": "/admin/usuarios/gestionar/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/admin/usuarios/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/admin/genero/",
                "method": "GET",
                "icono": "pi pi-user-minus",
                "link": "/admin/genero/",
                "titulo": "Generos",
                "items": [
                    {
                        "path": "/admin/gemero/gestionar/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/admin/genero/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/admin/tipo-identificacion/",
                "method": "GET",
                "icono": "pi pi-user-minus",
                "link": "/admin/tipo-identificacion/",
                "titulo": "T. Identificacion",
                "items": [
                    {
                        "path": "/admin/tipo-identificacion/gestionar/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/admin/tipo-identificacion/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/admin/reportes/",
                "method": "GET",
                "icono": "pi pi-user-minus",
                "link": "/admin/reportes/",
                "titulo": "Reportes",
                "items": [
                    {
                        "path": "/admin/reportes/ver/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/admin/reportes/ver/",
                        "titulo": "Gestionar",
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
        "titulo": "Encuestas",
        "items": [
            {
                "path": "/encuestas/preguntas/",
                "method": "GET",
                "icono": "icon",
                "link": "/encuestas/preguntas/",
                "titulo": "Preguntas",
                "items": [
                    {
                        "path": "/encuestas/preguntas/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/encuestas/preguntas/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/encuestas/momentos/",
                "method": "GET",
                "icono": "icon",
                "link": "/encuestas/momentos/",
                "titulo": "Momentos",
                "items": [
                    {
                        "path": "/encuestas/momentos/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/encuestas/momentos/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/encuestas/mis-encuestas/",
                "method": "GET",
                "icono": "icon",
                "link": "/encuestas/mis-encuestas/",
                "titulo": "Encuestas",
                "items": [
                    {
                        "path": "/encuestas/mis-encuestas/llenar-encuestas/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/encuestas/mis-encuestas/llenar-encuestas/",
                        "titulo": "Llenar Encuestas",
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
        "titulo": "PQRS",
        "items": [
            {
                "path": "/pqrs/solicitud/",
                "method": "GET",
                "icono": "icon",
                "link": "/pqrs/solicitud/",
                "titulo": "Solicitud",
                "items": [
                    {
                        "path": "/pqrs/solicitud/ver/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/ver/",
                        "titulo": "Ver",
                    },
                    {
                        "path": "/pqrs/solicitud/crear/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/crear/",
                        "titulo": "Crear",
                    },
                    {
                        "path": "/pqrs/solicitud/editar/",
                        "method": "PUT",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/editar/",
                        "titulo": "Editar",
                    },
                    {
                        "path": "/pqrs/solicitud/eliminar/",
                        "method": "DELETE",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/eliminar/",
                        "titulo": "Eliminar",
                    },
                    {
                        "path": "/pqrs/solicitud/mis-solicitudes/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/mis-solicitudes/",
                        "titulo": "Mis Solicitudes",
                    },
                ],
            },
            {
                "path": "/pqrs/tipo/",
                "method": "GET",
                "icono": "icon",
                "link": "/pqrs/tipo/",
                "titulo": "Tipo de solicitud",
                "items": [
                    {
                        "path": "/pqrs/tipo/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/pqrs/tipo/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/pqrs/asignacion/",
                "method": "GET",
                "icono": "icon",
                "link": "/pqrs/asignacion/",
                "titulo": "Asignacion",
                "items": [
                    {
                        "path": "/pqrs/asignacion/mis-solicitudes",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/pqrs/asignacion/mis-solicitudes",
                        "titulo": "Mis Solicitudes",
                    },
                    {
                        "path": "/pqrs/asignacion/solicitudes",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/pqrs/asignacion/solicitudes",
                        "titulo": "Solicitudes",
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
        "titulo": "Clasificados",
        "items": [
            {
                "path": "/clasificados/emprendimientos/",
                "method": "GET",
                "icono": "icon",
                "link": "/clasificados/emprendimientos/",
                "titulo": "Emprendimientos",
                "items": [
                    {
                        "path": "/clasificados/emprendimientos/crear/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/crear/",
                        "titulo": "Crear",
                    },
                    {
                        "path": "/clasificados/emprendimientos/ver/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/ver/",
                        "titulo": "Ver",
                    },
                    {
                        "path": "/clasificados/emprendimientos/editar/",
                        "method": "PUT",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/editar/",
                        "titulo": "Editar",
                    },
                    {
                        "path": "/clasificados/emprendimientos/eliminar/",
                        "method": "DELETE",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/eliminar/",
                        "titulo": "Eliminar",
                    },
                    {
                        "path": "/clasificados/emprendimientos/mis-emprendimientos/",
                        "method": "DELETE",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/mis-emprendimientos/",
                        "titulo": "Mis Emprendimientos",
                    },
                    {
                        "path": "/clasificados/emprendimientos/detalles/",
                        "method": "DELETE",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/detalles/",
                        "titulo": "Detalles",
                    },
                ],
            },
            {
                "path": "/clasificados/categoria/",
                "method": "GET",
                "icono": "icon",
                "link": "/clasificados/categoria/",
                "titulo": "Categorias",
                "items": [
                    {
                        "path": "/clasificados/categoria/gestionar",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/clasificados/categoria/gestionar",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/clasificados/sub-categoria/",
                "method": "GET",
                "icono": "icon",
                "link": "/clasificados/sub-categoria/",
                "titulo": "Subcategorias",
                "items": [
                    {
                        "path": "/clasificados/sub-categoria/gestionar",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/clasificados/sub-categoria/gestionar",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/clasificados/capacitaciones/",
                "method": "GET",
                "icono": "icon",
                "link": "/clasificados/capacitaciones/",
                "titulo": "Capacitaciones",
                "items": [
                    {
                        "path": "/clasificados/capacitaciones/gestionar",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/clasificados/capacitaciones/gestionar",
                        "titulo": "Gestionar",
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
        "titulo": "Eventos",
        "items": [
            {
                "path": "/eventos/actividades/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/actividades/",
                "titulo": "Actividades",
                "items": [
                    {
                        "path": "/eventos/actividades/ver/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/actividades/ver/",
                        "titulo": "Ver",
                    },
                    {
                        "path": "/eventos/actividades/crear/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/eventos/actividades/crear/",
                        "titulo": "Crear",
                    },
                    {
                        "path": "/eventos/actividades/editar/",
                        "method": "PUT",
                        "icono": "icon",
                        "link": "/eventos/actividades/editar/",
                        "titulo": "Editar",
                    },
                    {
                        "path": "/eventos/actividades/eliminar/",
                        "method": "DELETE",
                        "icono": "icon",
                        "link": "/eventos/actividades/eliminar/",
                        "titulo": "Eliminar",
                    },
                    {
                        "path": "/eventos/actividades/mis-actividades/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/actividades/mis-actividades/",
                        "titulo": "Mis Actividades",
                    },
                ],
            },
            {
                "path": "/eventos/areas/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/areas/",
                "titulo": "Areas",
                "items": [
                    {
                        "path": "/eventos/areas/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/areas/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/eventos/subareas/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/subareas/",
                "titulo": "Subareas",
                "items": [
                    {
                        "path": "/eventos/subareas/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/subareas/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/eventos/tipo-actividad/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/tipo-actividad/",
                "titulo": "Tipo Actividad",
                "items": [
                    {
                        "path": "/eventos/tipo-actividad/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/tipo-actividad/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/eventos/programa/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/programa/",
                "titulo": "Programas",
                "items": [
                    {
                        "path": "/eventos/programa/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/programa/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/eventos/sede/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/sede/",
                "titulo": "Sedes",
                "items": [
                    {
                        "path": "/eventos/sede/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/sede/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/eventos/facultad/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/facultad/",
                "titulo": "Facultades",
                "items": [
                    {
                        "path": "/eventos/facultad/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/facultad/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/eventos/asistencias/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/asistencias/",
                "titulo": "Asistencias",
                "items": [
                    {
                        "path": "/eventos/asistencias/ver-asistencias/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/asistencias/ver-asistencias/",
                        "titulo": "Ver Asistencias",
                    },
                    {
                        "path": "/eventos/asistencias/llenar-asistencias/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/asistencias/llenar-asistencias/",
                        "titulo": "LLenar Asistencias",
                    },
                ],
            },
        ],
    },
]

resources_egresado = [
    {
        "id_padre": 0,
        "path": "/inicio/",
        "icono": "pi pi-home",
        "method": "GET",
        "link": "/inicio/",
        "titulo": "Inicio",
        "items": [
            {
                "path": "/inicio/datos-personales/",
                "icono": "icon",
                "link": "/inicio/datos-personales/",
                "method": "GET",
                "titulo": "Datos Personales",
                "items": [
                    {
                        "path": "/inicio/datos-personales/actualizar-datos/",
                        "icono": "icon",
                        "method": "POST",
                        "link": "/inicio/datos-personales/actualizar-datos/",
                        "titulo": "Actualizar Datos",
                    },
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
        "titulo": "Encuestas",
        "items": [
            {
                "path": "/encuestas/mis-encuestas/",
                "icono": "icon",
                "method": "GET",
                "link": "/encuestas/mis-encuestas/",
                "titulo": "Mis Encuestas",
                "items": [
                    {
                        "path": "/encuestas/mis-encuestas/llenar-encuestas/",
                        "icono": "icon",
                        "method": "GET",
                        "link": "/encuestas/mis-encuestas/llenar-encuestas/",
                        "titulo": "LLenar encuestas",
                    },
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
        "titulo": "PQRS",
        "items": [
            {
                "path": "/pqrs/solicitud/",
                "icono": "icon",
                "link": "/pqrs/solicitud/",
                "titulo": "Solicitudes",
                "items": [
                    {
                        "path": "/pqrs/solicitud/crear/",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/crear/",
                        "titulo": "Crear",
                    },
                    {
                        "path": "/pqrs/solicitud/mis-solicitudes/",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/mis-solicitudes/",
                        "titulo": "Mis Solicitudes",
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
        "titulo": "Clasificados",
        "items": [
            {
                "path": "/clasificados/emprendimientos/",
                "icono": "icon",
                "method": "GET",
                "link": "/clasificados/emprendimientos/",
                "titulo": "Emprendimientos",
                "items": [
                    {
                        "path": "/clasificados/emprendimientos/ver",
                        "icono": "icon",
                        "method": "GET",
                        "link": "/clasificados/emprendimientos/ver",
                        "titulo": "Mostrar",
                    },
                    {
                        "path": "/clasificados/emprendimientos/crear",
                        "icono": "icon",
                        "method": "GET",
                        "link": "/clasificados/emprendimientos/crear",
                        "titulo": "Crear",
                    },
                    {
                        "path": "/clasificados/emprendimientos/mis-emprendimientos/",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/mis-emprendimientos/",
                        "titulo": "Mis Emprendimientos",
                    },
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
        "titulo": "Eventos",
        "items": [
            {
                "path": "/eventos/actividades/",
                "icono": "icon",
                "method": "GET",
                "link": "/eventos/actividades/",
                "titulo": "Actividades",
                "items": [
                    {
                        "path": "/eventos/actividades/mis-actividades/",
                        "icono": "icon",
                        "method": "GET",
                        "link": "/eventos/actividades/mis-actividades/",
                        "titulo": "Mis Actividades",
                    },
                ],
            },
        ],
    },
]