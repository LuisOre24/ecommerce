from app.models import Docente, Categoria, Modalidad
from rest_framework import serializers, viewsets
from .serializers import DocenteSerializer, CategoriaSerializer, ModalidadSerializer

class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ModalidadViewSet(viewsets.ModelViewSet):
    queryset = Modalidad.objects.all()
    serializer_class = ModalidadSerializer