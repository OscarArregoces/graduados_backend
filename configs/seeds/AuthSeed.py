from django.contrib.auth.hashers import make_password

GestoresSeed = [
    {"name": "FACEYA"},
    {"name": "FACED"},
    {"name": "FCSYH"},
    {"name": "FIUG"},
    {"name": "FCBYA Y DEPENDENCIAS"},
    {"name": "GENERAL"},
]

CondicionesSeed = [
    {"name": "Indígena"},
    {"name": "Victima de Violencia"},
    {"name": "Afrodescendientes"},
    {"name": "Condición de Discapacidad"},
    {"name": "Comunidad LGBTI"},
    {"name": "Violencia de Genero"},
    {"name": "Desplazado"},
    {"name": "Discapacitado"},
    {"name": "Grupos Religiosos"},
    {"name": "Ninguna"},
]
# CondicionesSeed = [
#     {"name": "Poblaciones étnicas"},
#     {"name": "Población con necesidades educativas especiales"},
#     {"name": "Población afectada por la violencia"},
#     {"name": "Niños, niñas y jóvenes trabajadores"},
#     {"name": "Adolescentes en conflicto con la ley penal"},
#     {"name": "Niños, niñas y adolescentes en protección"},
#     {"name": "Jóvenes y adultos iletrados"},
#     {"name": "Habitantes de frontera"},
#     {"name": "Población rural dispersa"},
#     {"name": "Ninguna"},
# ]

DocumentTypeSeed = [
    {"name": "Cédula de Ciudadanía"},
    {"name": "Tarjeta de Identidad"},
    {"name": "Registro Civil"},
    {"name": "Cédula de Extranjería"},
    {"name": "Carné de Identidad"},
    {"name": "Documento Nacional de Identidad"},
    {"name": "Pasaporte"},
    {"name": "Licencia de Conducción"},
    {"name": "Libreta Militar"},
    {"name": "Tarjeta Profesional"},
]

PersonsSeed = [
    {
        "fullname": "Usuario Administrador de Funcionarios",
        "identification": "1111111111",
        "address": "CARRERA 23 # 14 K 22",
        "nationality_id": 49,
        "departamento_id": 764,
        "municipio_id": 685,
        "email": "funcionarios@uniguajira.edu.co",
        "email2": "",
        "document_type_id": 1,
        "gender_type_id": 1,
        "graduado": False,
        "funcionario": True,
        "date_of_birth": "1999-08-28",
    },
    {
        "fullname": "Usuario Administrador de Graduados",
        "identification": "2222222222",
        "address": "Cll 15# 21-89",
        "nationality_id": 49,
        "departamento_id": 764,
        "municipio_id": 685,
        "document_type_id": 1,
        "gender_type_id": 1,
        "email": "graduados@uniguajira.edu.co",
        "email2": "",
        "graduado": False,
        "funcionario": True,
        "date_of_birth": "1999-08-28",
    },
]

UsersSeed = [
    {
        "username": "admin",
        "password": make_password("12345"),
        "is_staff": True,
        "person_id": 1,
    },
    {
        "username": "graduado",
        "password": make_password("12345"),
        "person_id": 2,
    },
]

GroupsSeed = [
    {"name": "Admin"},
    {"name": "General"},
    {"name": "Graduado"},
    {"name": "Funcionario General"},
]

GendersSeed = [
    {"name": "Hombre"},
    {"name": "Mujer"},
    {"name": "Otro"},
]

