from datetime import datetime

def formatDate(input_fecha):
    # Convertir la fecha de cadena a objeto datetime
    fecha_obj = datetime.strptime(str(input_fecha), "%Y-%m-%d %H:%M:%S")
    # 2008-05-01 
    # 2024-02-23
    
    # Formatear la fecha en el nuevo formato
    fecha_formateada = fecha_obj.strftime("Y%-%m-%d")
    
    return fecha_formateada
