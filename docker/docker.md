## Working with docker

    docker run -d -t --name name image

    docker ps

    docker exec -t myalpine ash

## Docker en ubuntu

    sudo apt install docker.io docker-compose

## Servidor web nginx

    sudo docker run --name web -itd -p 8080:80 nginx

## Servidor nginx con docker-compose

    sudo docker-compose ps
    sudo docker-compose up -d
    sudo docker-compose stop
    sudo docker-compose down