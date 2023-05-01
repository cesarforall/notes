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
