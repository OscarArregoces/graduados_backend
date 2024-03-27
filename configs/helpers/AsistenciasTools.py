from collections import defaultdict
from django.db.models import Count

from src.application.auth_module.models import Carrera, Persons
def CalcularConteoAsistencias(Asistencias):
    total_graduados = 0
    total_funcionarios = 0
    
    for persona in Asistencias:
        if persona['asistencia'] and persona['graduado']:
            total_graduados += 1
        elif persona['asistencia'] and persona['funcionario']:
            total_funcionarios += 1
    
    return total_graduados, total_funcionarios

def CalcularConteoExternos(Conteo_externos):
    resultados_externos = {}
    
    for item in Conteo_externos:
        vinculacion = item['vinculacion']
        conteo = item['conteo']
        resultados_externos[vinculacion] = conteo
        
    return resultados_externos

def CalcularImpactosAsistencias(Asistencias):
    confirmacion_asistencia = defaultdict(int)
    asistencia_real = defaultdict(int)
            
    for asistencia in Asistencias:
        # Contar confirmaciones de asistencia
        if asistencia.confirmacion:
            confirmacion_asistencia['confirmaron'] += 1
        else:
            confirmacion_asistencia['no_confirmaron'] += 1
                
        # Contar asistencias reales
        if asistencia.asistencia:
            asistencia_real['asistieron'] += 1
        else:
            asistencia_real['no_asistieron'] += 1
    return confirmacion_asistencia, asistencia_real

def CalcularConteoProgramas(Asistencias):
    asistencias_por_programa = Asistencias.values('user__person__carrera__programa').annotate(total_asistencias=Count('user__person__carrera__programa'))
    # asistencias_por_programa ahora contiene los resultados agrupados por programa
    total_programas = []
    for asistencia in asistencias_por_programa:
        programa = asistencia['user__person__carrera__programa']
        total_asistencias = asistencia['total_asistencias']
        total_programas.append({'programa': programa, 'total_asistencias': total_asistencias})
    return total_programas

def SepararGraduadosFuncionarios(Asistencias):
    asistencias_graduados = []
    asistencias_funcionarios = []
    for asistencia in Asistencias:
        if asistencia['asistencia'] and asistencia['graduado']:
            carreras = Carrera.objects.filter(person=asistencia['id'])
            for carrera in carreras:
                asistencias_graduados.append({
                    'fullname': asistencia['fullname'],
                    'programa': carrera.programa
                })
            # asistencias_graduados.append(asistencia)
        elif asistencia['asistencia'] and asistencia['funcionario']:
            asistencias_graduados.append({
                    'fullname': asistencia['fullname'],
                })
            asistencias_funcionarios.append(asistencia)
    return asistencias_graduados, asistencias_funcionarios
