## File descriptors (números)
Al enviar un comando a la shell enviamos un standard input. La respuesta correcta del comando (existe y se puede ejecutar) devuelve un standard output. Si la respuesta es errónea devueleve un standard error

stdin = 0
stout = 1
stderr = 2

## Redirecciones
Las redicciones exitosas (standard output) envían lo que contiene un fichero a un archivo

    ls Pictures > misarchivos.txt

Si repito el comando con otro directorio sobreescribo el archivo

    ls Downloads > misarchivos.txt

Para concatenar los datos se usa el soble operador

    ls Pictures > misarchivos.txt
    ls Downloads >> misarchivos.txt

Para redireccionar un error (standard error) se usa el file descriptor y operador de redirección

     ls kjsdkjdskj 2> error.txt

Para redireccionar un standard output y error en el mismo comando

    ls kjhfkjfjh >> output.txt 2>&1

Para redireccionar un standard input

    cat < archivo.txt

## Redirecciones con pipe operator |
Pipe operator nos permite convertir el standard output de un comando a standard input de otro comando

tee hace lo mismo que el símbolo >

    ls -lh | sort | tee output.txt | less

Para redirigir cowsay

    cowsay "Hello" | lolcat | tee cowsay.txt | less

## Operadores de control
; ejecuta de forma síncrona varios comandos

    ls ; mkdir dir ; cal

& ejecuta comandos de forma asíncrona

    ls & mkdir dir & cal

&& ejecuta comandos de manera condicional

    (si mkdir no da error se ejecuta cd)
    mkdir test && cd test

|| es el operador 'or' y ejecuta comando de manera secuencial

    cd mksmsksmk || echo

## Tipos de archivos

El comando 'ls' también muestra los permisos

| Atributo | Tipo de archivo |
|---|---|
|-|Archivo normal|
|d|Directorio|
|l|Link simbólico|
|b|Archivo de bloque especial. Contiene información de un dispositivo de almacenamiento como una memoria usb un disco duro externo|

## Tipos de permisos
Los unos y ceros son bits de modo octal

||r (read)|w (write)|x (execute)|Modo octal|
|---|---|---|---|---|
|Dueño|1|1|1|1^4 + 1^2 + 1^1 = 7|
|Grupo (user en la misma máquina)|1|0|1|1^4 + - + 1^1 = 5|
|World (otros)|1|0|1|1^4 + - + 1^1 = 5|

## Modo octal

|Octal|Binario|Permisos|
|---|---|---|
|0|000|---|
|1|001|--x|
|2|010|-w-|
|3|011|-wx|
|4|100|r--|
|5|101|r-x|
|6|110|rw-|
|7|111|rwx|

## Modo simbólico
Los símbolos que cambian los permisos según el usuario

|Símbolo|Significado|
|---|---|
|u|Solo el ususario|
|g|Solo para el grupo|
|o|Solo para otros (World)|
|a|Aplica para todos|



## Cómo modificar permisos en la terminal de forma octal

Con el usuario root activo (ejecutar sudo su)

    chmod 000 file.ext

## Cómo modificar permisos en la terminal con modo simbólico

Para quitar permisos se usa el modo simbólico - y tipo de permiso

    chmod u-r file.ext

Para añadir permisos se usa el modo simbólico + y el tipo de permiso

    chmod o+r file.ext

Para modificar distintos permisos con módo simbólico se usa la coma ',' sin separación

    chmod o+r,u-r file.ext

## Cambiar de usuario

El comando su cambia de usuario en la termina

    su root

## Link simbólico
Es un tipo de archivo que hace referencia a algún lugar. Se estructura con ln -s (simbólico) path y nombre

    ln -s Desktop/dev Desarrollo
    cd Desarrollo

## Variables de entorno
Las variables de entorno nos permiten tener configuraciones guardadas permanentemente
Para imprimir variables de entorno se usa echo $NOMBREDELAVARIABLE

    echo $HOME

## Cómo modificar las variables de entorno y alias
Editar el archivo oculto que corresponda al shell que se usa, por ejemplo, .bashrc

    code .bashrc

Añadir la nueva ruta de binarios con ':' y guardar

    PATH=$PATH:/ruta/de/bin/

Ejecutar bash

## Bin
Los archivos binarios son programitas ejecutables

## Wildcards
El símbolo *.ext se traduce en archivo con cualquier nombre que contenga lo siguiente al final

## Comnados de búsqueda
El comando find busca los archivos que contenga un nombre desde una ruta dada

    find ./ -name *.txt | less

Para buscar por tipos puede tener como argumento f o d

    find ./ -type d -name Documents
    find ./ -type f -name text

Para buscar todos los archivos .log (archivos con información o registros de programas sin importancia)

    find ruta -type f -name *.log

Para buscar archivos por tamaño

    find ./ -size 20M

## Comando grep
Global Regular Expresion Print usa expresiones regulares (regex) para hacer búsquedas

    grep regex file.ext

El comando grep es key sensitive. Para evitarlo añadimos la opción -i

    grep -i the movies.csv

La opción c cuenta las coincidencias de un regex en la búsqueda

    grep -c the movies.csv

Para juntar varias opciones se escribe el guión una vez y las opciones van seguidas

    grep -ic the movies.csv

La opción v muestra los datos que no cumplan el regex

    grep -vi towers movies.csv

## Utilidades de red
El comando ifconfig muestra las características de red
Para usar el comando en wsl hace falta instalar net-tools

    sudo apt install net-tools

El comando tracer route muestra las máquinas por las que viaja un archivo antes de llegar a la nuestra

Hace falta instalarlo con

    sudo apt-get update
    sudo apt-get install traceroute
