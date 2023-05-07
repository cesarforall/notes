    version: '3'
    services:
    django:
        build:
        context: ./django  # Ruta al directorio del proyecto Django
        dockerfile: Dockerfile  # Nombre del archivo Dockerfile para Django
        ports:
        - 8000:8000  # Puerto de exposición para el servidor Django
        depends_on:
        - db  # Dependencia en el servicio de la base de datos PostgreSQL
        volumes:
        - ./django:/app  # Volumen para montar el código fuente de Django en el contenedor
        command: python manage.py runserver 0.0.0.0:8000  # Comando para ejecutar el servidor Django

    react:
        build:
        context: ./react  # Ruta al directorio del proyecto React
        dockerfile: Dockerfile  # Nombre del archivo Dockerfile para React
        ports:
        - 3000:3000  # Puerto de exposición para la aplicación React
        volumes:
        - ./react:/app  # Volumen para montar el código fuente de React en el contenedor
        command: npm start  # Comando para ejecutar la aplicación React

    db:
        image: postgres:latest  # Imagen de Docker para PostgreSQL
        environment:
        - POSTGRES_USER=usuario  # Nombre de usuario de PostgreSQL
        - POSTGRES_PASSWORD=contraseña  # Contraseña de PostgreSQL
        - POSTGRES_DB=basededatos  # Nombre de la base de datos PostgreSQL
        volumes:
        - pgdata:/var/lib/postgresql/data  # Volumen para persistir los datos de PostgreSQL

    volumes:
    pgdata:  # Volumen para persistir los datos de PostgreSQL
