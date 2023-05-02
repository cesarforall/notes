## docker-compose

- https://dev.to/elalemanyo/how-to-install-docker-and-docker-compose-on-raspberry-pi-1mo

El plugin de compose se instala mejor de forma manual.

- https://docs.docker.com/compose/install/linux/#install-the-plugin-manually

## Cómo funciona

docker-compose es un plugin que usa docker para organizar y ejecutar diferentes contenedores

Se configura en un archivo .yml definiendo distintos servicios. Cada servicio es un contenedor

    version: '3.3'

    services:
    postgres:
        image: postgres:13
        environment:
        - POSTGRES_DB=my_store
        - POSTGRES_USER=cesar
        - POSTGRES_PASSWORD=admin123
        ports:
        - 5432:5342

Se ejecuta con el comando

    sudo docker-compose up -d postgres

Se ven las imágenes corriendo con el comando:

    sudo docker-compose ps

Se baja el servicio con:

    sudo docker-compose down

## Estado
Los contenedores de docker son stateless. Es decir, cuando el servicio se baja, todo lo realizado interiormente se elimina.

## Persistencia de datos
Para tener persistencia de datos con Docker se configura compose con volumes. Esta especificación configura una ruta donde almacenar datos.

- https://hub.docker.com/_/postgres


    version: '3.3'

    services:
    postgres:
        image: postgres:13
        environment:
        - POSTGRES_DB=my_store
        - POSTGRES_USER=cesar
        - POSTGRES_PASSWORD=admin123
        ports:
        - 5432:5342
        volumes:
        - ./postgres_data:/var/lib/postgresql/data

## Entrar en un contenedor via terminal
Iniciar el servicio

    docker compose up -d nombre_del_servicio

Entrar en el contenedor

    docker compose exec nombre_del_servicio bash

## Trabajar con Postgress
Crear una base de datos

    psql -h localhost -d my_store -U cesar

Ver la estructura de la base de datos

    \d+

Salir de la base de datos

    \q
