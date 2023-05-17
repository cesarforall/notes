## docker-compose.yml
Este archivo sirve para configurar la relación entre contenedores

    version: "3"
    services:
    web:
        build: 
        context: ./backend
        restart: always
        ports:
        - "8000:8000"
        depends_on:
        - db

    db:
        image: postgres
        restart: always
        environment:
        POSTGRES_USER: your_username
        POSTGRES_PASSWORD: your_password
        POSTGRES_DB: your_database

    frontend:
        build:
        context: ./frontend
        dockerfile: Dockerfile
        restart: always
        ports:
        - "3000:3000"
        environment:
        NODE_ENV: development
        depends_on:
        - web

    volumes:
    postgres_data:


## Dockerfile
Este archivo sirve para definir como se construye una imagen de contenedor

    # Establecer la imagen base
    FROM python:3.9

    # Establecer el directorio de trabajo en el contenedor
    WORKDIR /app

    # Copiar los archivos de la aplicación al directorio de trabajo en el contenedor
    COPY . /app

    # Instalar las dependencias de la aplicación
    RUN pip install --no-cache-dir -r requirements.txt

    # Exponer el puerto en el contenedor (opcional)
    EXPOSE 8000

    # Comando para iniciar el servidor de desarrollo de Django
    CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


## requirements.txt
Este archivo especifica los paquetes de Python a instalar en un contenedor

    Django>=3.2.0
    psycopg2-binary>=2.8.6
