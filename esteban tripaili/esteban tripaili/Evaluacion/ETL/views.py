from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import RawData, Persona
from .serializers import RawDataSerializer, PersonaSerializer
from datetime import datetime

@api_view(['POST'])
def transformar_datos(request):
    raw_data_id = request.data.get('raw_data_id')

    try:
        raw_data = RawData.objects.get(id=raw_data_id)
    except RawData.DoesNotExist:
        return Response({'error': 'Datos no encontrados'}, status=status.HTTP_404_NOT_FOUND)

    # Calcular edad nominal
    nacimiento = raw_data.edad
    hoy = datetime.today()
    edad_nominal = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))

    nombre_completo = f"{raw_data.nombre} {raw_data.apellido}"

    persona = Persona(nombre_completo=nombre_completo, edad_nominal=edad_nominal)
    persona.save()

    return Response(PersonaSerializer(persona).data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def obtener_personas(request):
    personas = Persona.objects.all()
    serializer = PersonaSerializer(personas, many=True)
    return Response(serializer.data)
