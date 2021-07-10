from .models import Rams, Distribuidor
from rest_framework import serializers

class DistribuidorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Distribuidor
        fields ='__all__'

class RamsSerializer(serializers.ModelSerializer):
    nombre_distribuidor =serializers.CharField(read_only=True, source="Distribuidor.nombre")
    Distribuidor = DistribuidorSerializer(read_only=True)
    nombre = serializers.CharField(required=True, min_length=3)

    class Meta:
        model = Rams
        fields = '__all__'