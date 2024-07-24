from rest_framework import serializers
from .models import RawData, Persona

class RawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawData
        fields = ['id', 'nombre', 'apellido', 'edad']

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'nombre_completo', 'edad_nominal']
