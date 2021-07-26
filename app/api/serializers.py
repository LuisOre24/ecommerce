from app.models import Docente, Categoria, Modalidad
from rest_framework import serializers

class DocenteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Docente
        fields = ['id', 'nombres', 'apellidos', 'especialidad', 'celular', 'email']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'categoria']

class ModalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modalidad
        fields = ['id', 'modalidad']

        

