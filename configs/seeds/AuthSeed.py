from django.contrib.auth.hashers import make_password

GestoresSeed = [
    {"name": "FACEYA"},
    {"name": "FACED"},
    {"name": "FCSYH"},
    {"name": "FIUG"},
    {"name": "FCBYA Y DEPENDENCIAS"},
]

CondicionesSeed = [
    {"name": "INDIGENA"},
    {"name": "AFROCOLOMBIANO"},
    {"name": "CONDICION DE DISCAPACIDAD"},
    {"name": "COMUNIDAD LGBTI"},
    {"name": "VICTIMA DE VIOLENCIA"},
    {"name": "VIOLENCIA DE GENERO"},
]
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
        "nationality": "Colombia",
        "email": "funcionarios@uniguajira.edu.co",
        "email2": "",
        "document_type_id": 1,
        "gender_type_id": 1,
    },
    {
        "fullname": "Usuario Administrador de Graduados",
        "identification": "2222222222",
        "address": "Cll 15# 21-89",
        "nationality": "Colombia",
        "document_type_id": 1,
        "gender_type_id": 1,
        "email": "graduados@uniguajira.edu.co",
        "email2": "",
    },
]

CarrerasSeed = [
    {
        "programa": "INGENIERÍA DE SISTEMAS",
        "modalidad_grado": "INFORME DE INVESTIGACIÓN",
        "proyecto_grado": "ANÁLISIS DEL NIVEL DE SATISFACCIÓN DE LOS ESTUDIANTES DE LA UNAD Y EL SENA, FRENTE AL USO DE AMBIENTES VIRTUALES DE APRENDIZAJE (AVA), EN EL MUNICIPIO DE RIOHACHA.",
        "periodo_grado": "2023 II",
        "numero_acta": "24313",
        # "fecha_grado": "2023/12/11",
        "numero_folio": "182",
        "sede": "RIOHACHA",
        "direccion_intitucional": "KM 5 VIA MAICAO",
        "person_id": 1,
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
    {"name": "Graduado"},
    {"name": "General"},
]

GendersSeed = [
    {"name": "Masculino"},
    {"name": "Femenino"},
    {"name": "Otro"},
]
