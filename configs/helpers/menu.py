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
        "titulo": "Administrador",
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
                        "titulo": "Administrativos",
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
                "titulo": "Graduados",
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
                        "titulo": "Mis Encuestas",  
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
                        "path": "/pqrs/solicitud/crear/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/crear/",
                        "titulo": "Generar",   
                    },
                    {
                        "path": "/pqrs/solicitud/ver/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/ver/",
                        "titulo": "Ver",   
                    },
                    {
                        "path": "/pqrs/solicitud/editar/",
                        "method": "PUT",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/editar/",
                        "titulo": "Actualizar",   
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
                "titulo": "Tipo de Solicitud",   
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
                "titulo": "Asignación",  
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
                        "path": "/eventos/actividades/crear/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/eventos/actividades/crear/",
                        "titulo": "Solicitar",   
                    },
                    {
                        "path": "/eventos/actividades/aprobacion/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/actividades/aprobacion/",
                        "titulo": "Aprobación",  
                    },
                    {
                        "path": "/eventos/actividades/ver/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/actividades/ver/",
                        "titulo": "Reportes", 
                    },
            
                    {
                        "path": "/eventos/actividades/editar/",
                        "method": "PUT",
                        "icono": "icon",
                        "link": "/eventos/actividades/editar/",
                        "titulo": "Actualizar", 
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
                    {
                        "path": "/eventos/actividades/asistencias/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/actividades/asistencias/",
                        "titulo": "Asistencias",   
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
    {"id":55},
    {"id":58},
]