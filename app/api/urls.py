from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import DocenteViewSet, CategoriaViewSet, ModalidadViewSet

router = DefaultRouter()
router.register('docentes', DocenteViewSet)
router.register('categorias', CategoriaViewSet)
router.register('modalidades', ModalidadViewSet)

urlpatterns = [
    path('', include(router.urls))
]