from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializar):
    class Meta:
        model = Tarea
        fields = ['id','titulo', 'descripcion', 'completado']
        read_only_fields = ['id']

    
    