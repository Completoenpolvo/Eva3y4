from django.urls import path
from .views import transformar_datos, obtener_personas

urlpatterns = [
    path('transformar_datos/', transformar_datos, name='transformar_datos'),
    path('datos_transformados/', obtener_personas, name='obtener_personas'),
]
