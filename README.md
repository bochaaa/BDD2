# BDD2

# 1. Instalar python (3.12)

# 2. Entorno virtual :

 Creal en env

-py -3 -m venv .venv  

 Activar el env

-.venv\Scripts\Activate.ps1  # activamos el entorno virtual

-python -m pip install --upgrade pip

# 3. Instalar Django

-pip install django

# 4. Instalar dependencias
   -pip install -r requirements.txt

# 5. Ejecutar en desarrollo

   -python manage.py runserver


# 6. Endpoints de Prueba 

POST /api/clientes/ → Crear (ALTA)

GET /api/clientes/ → Listar

GET /api/clientes/{id}/ → Detalle

PUT/PATCH /api/clientes/{id}/ → Modificar (MODIFICACIÓN)

DELETE /api/clientes/{id}/ → Eliminar (BAJA)
