ls -> hace un lista de todo lo que hay visible en el directorio

less archivo.ext -> permite navegar por un archivo
    - ⬆️ y ⬇️ para navegar por el archivo
    - spacebar para moverse más rápido
    - /loquequierobuscar caracter para buscar caracteres
    - q (quit) para salir de less

echo "string" -> genera un standard output en la terminal

El comando cat ejecuta un editor de texto sencillo. Para salir pulsar Ctrl + d.

    cat > text.txt

cat archivo.ext archivo.ext -> muestra en consola la concatenación de los archivos

cowsay "string" -> muestra un mensaje con una vaca

echo "string" | lolcat -> muestra un color en el texto en consola
    cowsay -f gnu No me puedo creer que haya otra vaca | lolcat

cal -> muestra un calendario

El operador de redirección > hace lo mismo que el comando touch cuando no lleva stdin

    > archivo.txt

sudo su -> cambia al usuario al modo root

- exit -> para salir del modo root

whoami -> muestra el usuario actual

id -> muestra el nombre del usuario

    id
    uid=1000(user)...

su user -> (switch user) cambia de usuario en la terminal

    su root

pwd -> (print working directory) muestra la ruta del directorio actual en el sistema de archivos

passwd -> cambia la contraseña del usuario actual

sudo -> da permisos de usuario root al usuario actual

sudo su -> cambia el usuario actual a root

printenv -> muestra todas las variables de entorno guardadas

echo $PATH -> imprime todas las rutas de los binarios que ejecuta el sistema

type comando -> muestra el tipo de comando

which comando -> busca la ruta de un comando

find ./ruta -name nombredearchivo -> busca las rutas donde se encuentra un archivo con el nombre descrito empezando por la ruta inicial

wc -> (word count) cuenta las palabras que hay en un archivo

ifconfig -> muestra las características de red

ping website -> devuelve constantemente la respuesta de una página web

curl website -> trae un archivo en text a partir de la red

wget website -> (web get) descarga el archivo html

wget -O name.ext -> descarga lo que hay una ruta con un nuevo nombre

traceroot website -> muestra todas las computadoras por donde pasa la información

netstat -i -> muestra los dispositivos de red