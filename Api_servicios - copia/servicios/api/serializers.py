from rest_framework import serializers
from .models import servicio_riego, goteo, riego_invernadero, riego_jardines, aspersion, conducciones, riego_Arboles, riego_tecnificados

class goteoSerializer(serializers.ModelSerializer):
    class Meta:
        model = goteo
        fields = '__all__'

class riego_invernaderoSerializer(serializers.ModelSerializer):
    class Meta:
        model = riego_invernadero
        fields = '__all__'

class riego_jardinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = riego_jardines
        fields = '__all__'

class aspersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = aspersion
        fields = '__all__'

class conduccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = conducciones
        fields = '__all__'

class riego_ArbolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = riego_Arboles
        fields = '__all__'

class riego_tecnificadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = riego_tecnificados
        fields = '__all__'

class servicio_riegoSerializer(serializers.ModelSerializer):
    id_goteo = goteoSerializer()
    id_riego_invernadero = riego_invernaderoSerializer()
    id_riego_jardines = riego_jardinesSerializer()
    id_aspersion = aspersionSerializer()
    id_conducciones = conduccionesSerializer()
    id_riego_Arboles = riego_ArbolesSerializer()
    id_riego_tecnificados = riego_tecnificadosSerializer()

    class Meta:
        model = servicio_riego
        fields = '__all__'
