
from configs.const.condicionesVulnerables import CondicionesVulnerablesConst


def formateGenderType(gender):
    if(gender == 'HOMBRE'):
        return 1
    elif (gender == 'MUJER'):
        return 2
    else:
        return None

def formateDocumentType(typeDocument):
    if(typeDocument == 'C'):
        return 1
    elif (typeDocument == 'CC'):
        return 1
    elif (typeDocument == 'CE'):
        return 4
    elif (typeDocument == "TI"):
        return 2
    else:
        return None

def formateNationaliy(nationality):
    if(nationality == 'ARGENTINA'):
        return 49
    elif (nationality == 'BRASIL'):
        return 49
    elif (nationality == 'ECUADOR'):
        return 49
    elif (nationality == 'ESPAÑA'):
        return 49
    elif (nationality == 'VENEZUELA'):
        return 49
    elif (nationality == 'COLOMABIA' or nationality == 'COLOMBA' or nationality == 'COLOMBIA' ):
        return 49
    else:
        return 49

def formateDepartamento(departamento):
    return 764
def formateMunicipio(municipio):
    return 685
def formateCondicionVulnerable(condition):
    if(condition in CondicionesVulnerablesConst[0]['opciones'] ):
        return CondicionesVulnerablesConst[0]['value']
    elif (condition in CondicionesVulnerablesConst[1]['opciones']):
        return CondicionesVulnerablesConst[1]['value']
    elif (condition in CondicionesVulnerablesConst[2]['opciones']):
        return CondicionesVulnerablesConst[2]['value']
    elif (condition in CondicionesVulnerablesConst[3]['opciones']):
        return CondicionesVulnerablesConst[3]['value']
    elif (condition in CondicionesVulnerablesConst[4]['opciones']):
        return CondicionesVulnerablesConst[4]['value']
    elif (condition in CondicionesVulnerablesConst[5]['opciones']):
        return CondicionesVulnerablesConst[5]['value']
    elif (condition in CondicionesVulnerablesConst[6]['opciones']):
        return CondicionesVulnerablesConst[6]['value']
    else:
        return CondicionesVulnerablesConst[6]['value']
