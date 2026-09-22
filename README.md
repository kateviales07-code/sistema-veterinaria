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


## Funcionalidades

El sistema permite registrar propietarios, mascotas y consultas veterinarias.

También cuenta con filtros, paginación, autenticación y permisos para controlar el acceso a algunos endpoints.


## Reflexión final 
El proceso inicia cuando Postman envía la solicitud POST a la URL de la API, la cual redirige la petición hacia la View. Allí, la vista recibe la información y se la entrega al Serializer para ejecutar la validación del contenido. Una vez comprobado que los datos son correctos, el Serializer se apoya en el Model y utiliza el ORM para procesar la creación del registro y persistirlo en la base de datos. Finalmente, se toma la información procesada para estructurar y devolver una Response HTTP en formato JSON con la confirmación de la consulta registrada.

## 16. Documentación de la API

| Método | URL | Descripción | Parámetros / Body | Respuesta (Ejemplo Real) | Códigos |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/clinica/api/mascotas/` | Obtiene el listado paginado de las mascotas registradas en el sistema. | Query params:<br>`?page=1` | `{"pagina_actual": 1, "total_paginas": 2, "total_mascotas": 8, "resultados": [{"id": 1, "nombre": "Coco", "especie": "Gato", "raza": "persa", "fecha_nacimiento": "2025-05-22", "peso": "4.00", "activo": true, "propietario": 1}]}` | `200 OK` |
| **POST** | `/clinica/api/mascotas/` | Registra una nueva mascota asociada a un propietario. | **Body (JSON):**<br>`{"nombre": "Luna", "especie": "Perro", "raza": "Labrador", "fecha_nacimiento": "2023-01-15", "peso": 12.50, "activo": true, "propietario": 1}` | `{"id": 10, "nombre": "Luna", "especie": "Perro", "raza": "Labrador", "fecha_nacimiento": "2023-01-15", "peso": "12.50", "activo": true, "propietario": 1}` | `201 Created`<br>`400 Bad Request` |
| **GET** | `/clinica/api/mascotas/{id}/` | Muestra el detalle completo de una mascota específica según su ID. | URL Param: `id` | `{"id": 10, "nombre": "Luna", "especie": "Perro", "raza": "Labrador", "fecha_nacimiento": "2023-01-15", "peso": "12.50", "activo": true, "propietario": 1}` | `200 OK`<br>`404 Not Found` |
| **GET** | `/clinica/api/propietarios/` | Lista todos los propietarios de mascotas registrados en el sistema. | N/A | `[{"id": 1, "identificacion": "504050298", "nombre": "Joan", "telefono": "65432891", "email": "joan@gmail.com"}, {"id": 2, "identificacion": "609830275", "nombre": "Yale", "telefono": "76548901", "email": "yale@gmail.com"}]` | `200 OK` |
