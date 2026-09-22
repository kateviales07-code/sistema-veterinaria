# Sistema de Gestión Veterinaria

Proyecto realizado en Django para llevar el registro de propietarios, mascotas y consultas veterinarias.

## Requisitos

- Python
- Django
- Django REST Framework

## Instalación

Crear el entorno virtual:

python -m venv .venv

Activar el entorno virtual:

.venv\Scripts\activate

Instalar Django:

python -m pip install "Django>=5.2,<5.3"

Instalar Django REST Framework:

pip install djangorestframework

## Migraciones

Para crear y aplicar las migraciones:

python manage.py makemigrations
python manage.py migrate

## Ejecutar el proyecto

Para iniciar el servidor:

python manage.py runserver

## Pruebas

Para ejecutar las pruebas:

python manage.py test

##Reflexión final 
El proceso inicia cuando Postman envía la solicitud POST a la URL de la API, la cual redirige la petición hacia la View. Allí, la vista recibe la información y se la entrega al Serializer para ejecutar la validación del contenido. Una vez comprobado que los datos son correctos, el Serializer se apoya en el Model y utiliza el ORM para procesar la creación del registro y persistirlo en la base de datos. Finalmente, se toma la información procesada para estructurar y devolver una Response HTTP en formato JSON con la confirmación de la consulta registrada.

## Funcionalidades

El sistema permite registrar propietarios, mascotas y consultas veterinarias.

También cuenta con filtros, paginación, autenticación y permisos para controlar el acceso a algunos endpoints.
