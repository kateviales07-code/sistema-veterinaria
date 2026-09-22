from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token

from .serializers import MascotaSerializer, ConsultaVeterinariaSerializer
from .models import Propietario, Mascota


class PruebasAutomatizadasTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.propietario = Propietario.objects.create(
            identificacion="123456789",
            nombre="Propietario Test",
            telefono="88888888",
            email="test@test.com"
        )

        
        self.mascota = Mascota.objects.create(
            nombre="Firulais",
            especie="Perro",
            raza="Poodle",
            fecha_nacimiento="2020-01-01",
            peso=10.50,
            propietario=self.propietario
        )

        
        self.usuario_regular = User.objects.create_user(
            username="regular_test",
            password="password123"
        )
        self.token_regular = Token.objects.create(user=self.usuario_regular)

  
        self.usuario_admin = User.objects.create_user(
            username="admin_test",
            password="password123",
            is_staff=True
        )
        self.token_admin = Token.objects.create(user=self.usuario_admin)

    
    def test_mascota_serializer_peso_cero_invalido(self):
        datos = {
            "nombre": "Bobby",
            "especie": "Perro",
            "raza": "Mestizo",
            "fecha_nacimiento": "2021-05-10",
            "peso": 0,  # Peso en 0
            "propietario": self.propietario.id
        }
        serializer = MascotaSerializer(data=datos)
        self.assertFalse(serializer.is_valid())
        self.assertIn('peso', serializer.errors)

    
    def test_consulta_serializer_costo_negativo_invalido(self):
        datos = {
            "mascota": self.mascota.id,
            "motivo": "Revision de rutina",
            "diagnostico": "Saludable",
            "tratamiento": "Ninguno",
            "costo": -50.00  
        }
        serializer = ConsultaVeterinariaSerializer(data=datos)
        self.assertFalse(serializer.is_valid())
        self.assertIn('costo', serializer.errors)

    
    def test_perfil_usuario_anonimo_rechazado(self):
        response = self.client.get('/clinica/api/perfil/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    
    def test_perfil_usuario_autenticado_exitoso(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_regular.key)
        response = self.client.get('/clinica/api/perfil/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_estadisticas_permisos_por_rol(self):
      
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_regular.key)
        response_regular = self.client.get('/clinica/api/estadisticas/')
        self.assertEqual(response_regular.status_code, status.HTTP_403_FORBIDDEN)

        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_admin.key)
        response_admin = self.client.get('/clinica/api/estadisticas/')
        self.assertEqual(response_admin.status_code, status.HTTP_200_OK)