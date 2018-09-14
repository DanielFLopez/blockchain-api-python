Instrucciones de instalación:
=============================

Clonar el repositorio.

Crear una base de datos en PostgreSQL con las credenciales especificadas en el settings.

Crear un virtualenv, para mayor comodidad se recomienda utilizar virtualenvwrapper.

Instalar los requirements en el virtualenv

    pip install -r requirements.txt

Crear las migraciones

    python manage.py makemigrations

Correr las migraciones::

    python manage.py migrate

Correr el siguiente comando el cual crear el bloque inicial

    python manage.py shell < api/initialize.py
    
Correr el comando para cargar la cuenta incial
    
    python manage.py loaddata initial_data

Correr el servidor

    python manage.py runserver

la direccion del proyecto esta definida en el settings base, se debe acceder por la ruta

    localhost:8000

Instrucciones para medir la cobertura de los test:
============================================================

Se debe tener el coverage instalado en el ambiente virtual, una vez en la carpeta del proyecto se debe correr el
siguiente comando con el ambiente activo

    coverage run manage.py test

Para ver los resultados por la consola se debe usar el siguiente comando

    coverage report

Para generar los archivos html del coverage se debe usar el siguiente comando

    coverage html
    
==================================================

- django-rest-framework: http://www.django-rest-framework.org/
- coverage: https://bitbucket.org/ned/coveragepy/overview