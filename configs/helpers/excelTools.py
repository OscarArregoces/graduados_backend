
def formateGenderType(gender):
    if(gender == 'HOMBRE'):
        return 1
    elif (gender == 'MUJER'):
        return 2
    else:
        return None

def formateDocumentType(type):
    if(type == 'C'):
        return 1
    elif (type == 'CC'):
        return 1
    elif (type == 'CE'):
        return 4
    elif (type == "TI"):
        return 2
    else:
        return None

def formateNationaliy(nationality):
    if(nationality == 'ARGENTINA'):
        return "Argentina"
    elif (nationality == 'BRASIL'):
        return "Brasil"
    elif (nationality == 'ECUADOR'):
        return "Ecuador"
    elif (nationality == 'ESPAÑA'):
        return "España"
    elif (nationality == 'VENEZUELA'):
        return "Venezuela"
    elif (nationality == 'COLOMABIA' or nationality == 'COLOMBA' or nationality == 'COLOMBIA' ):
        return "Colombia"
    else:
        return ""

def formateCondition(condition):
    if(condition == 1):
        return "Soltero(a)"
    elif (condition == 2):
        return "Casado(a)"
    elif (condition == 3):
        return "Divorciado(a)"
    elif (condition == 4):
        return "Viudo(a)"
    elif (condition == 5):
        return "Unión Libre"
    elif (condition == 6):
        return "Religioso(a)"
    elif (condition == 8):
        return "Separado(a)"
    else:
        return ""
