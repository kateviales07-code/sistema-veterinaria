from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Propietario, Mascota, ConsultaVeterinaria
from .serializers import (
    PropietarioSerializer,
    MascotaSerializer,
    ConsultaVeterinariaSerializer
)

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

#Contador
@api_view(['GET'])
def api_sesion(request):
    visitas = request.session.get('visitas', 0) + 1
    request.session['visitas'] = visitas
    return Response({
        "mensaje": "Contador de accesos incrementado",
        "visitas": visitas
    })


# Endpoint protegido de perfil
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def perfil(request):
    return Response({
        "id": request.user.id,
        "username": request.user.username,
        "email": request.user.email
    })

# Endpoint administrativo de estadísticas
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def estadisticas(request):
    return Response({
        "total_propietarios": Propietario.objects.count(),
        "total_mascotas": Mascota.objects.count(),
        "mascotas_activas": Mascota.objects.filter(activo=True).count(),
        "total_consultas": ConsultaVeterinaria.objects.count()
    })


def inicio(request):
    return HttpResponse("API de Gestión Veterinaria activa")



@api_view(['GET', 'POST'])
def api_mascotas(request):

    if request.method == 'GET':
        mascotas = Mascota.objects.all().order_by('id')
        serializer = MascotaSerializer(mascotas, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MascotaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def detalle_mascota(request, pk):

    try:
        mascota = Mascota.objects.get(pk=pk)

    except Mascota.DoesNotExist:
        return Response(
            {'error': 'Mascota no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )


    if request.method == 'GET':
        serializer = MascotaSerializer(mascota)

        return Response(serializer.data)


    if request.method == 'PUT':
        serializer = MascotaSerializer(
            mascota,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    if request.method == 'PATCH':
        serializer = MascotaSerializer(
            mascota,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == 'DELETE':
        mascota.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

@api_view(['GET', 'POST'])
def api_propietarios(request):

    if request.method == 'GET':
        propietarios = Propietario.objects.all().order_by('id')

        serializer = PropietarioSerializer(
            propietarios,
            many=True
        )

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PropietarioSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



@api_view(['GET', 'POST'])
def api_consultas(request):

    if request.method == 'GET':
        consultas = ConsultaVeterinaria.objects.all().order_by('id')

        serializer = ConsultaVeterinariaSerializer(
            consultas,
            many=True
        )

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ConsultaVeterinariaSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

from rest_framework import generics
from .models import Mascota
from .serializers import MascotaSerializer
from .pagination import MascotaPagination  

#class MascotaListAPIView(generics.ListAPIView):
    #queryset = Mascota.objects.all()
    #serializer_class = MascotaSerializer
    #pagination_class = MascotaPagination  


class MascotaListAPIView(generics.ListCreateAPIView):
    serializer_class = MascotaSerializer
    pagination_class = MascotaPagination

    def get_queryset(self):
        queryset = Mascota.objects.all()

        
        especie = self.request.query_params.get('especie')
        activas = self.request.query_params.get('activas')
        propietario = self.request.query_params.get('propietario')

        
        if especie:
            queryset = queryset.filter(especie__iexact=especie)

        
        if activas is not None:
            es_activa = activas.lower() == 'true'
            queryset = queryset.filter(activo=es_activa)

        
        if propietario:
            queryset = queryset.filter(propietario_id=propietario)

        return queryset