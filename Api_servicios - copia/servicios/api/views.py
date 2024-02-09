from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers  # Se corrigió la importación
from .models import servicio_riego
from .serializers import servicio_riegoSerializer  # Se asume que el serializador está definido en el archivo serializers.py en el mismo directorio


@api_view()
def inicio(request):
    servicios = servicio_riego.objects.all()
    serializer = servicio_riegoSerializer(servicios, many=True)
    return Response(serializer.data)


def tabla(request):
    servicios = servicio_riego.objects.all()
    return render(request, 'tabla.html', {'servicios': servicios})