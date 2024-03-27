# Importa la función render_to_string
from django.template.loader import render_to_string

# Importa la función send_mail
from django.core.mail import send_mail

# Importa la función JsonResponse si estás utilizando Django Rest Framework
from django.http import JsonResponse

def EnviarCorreos(destinatarios, asunto, template, contexto):
    mensaje_html = render_to_string(template, contexto)
    send_mail(
        asunto,
        '',
        'oiarregoces@uniguajira.edu.co',
        destinatarios,
        html_message=mensaje_html,
    )
    return JsonResponse({'mensaje': 'Correo enviado exitosamente'})
