## Qué es la shell
La terminal es la ventana que aloja la shell.
La shell es un programa que toma comandos, los interpreta y los pasa al sistema operativo para hacer algo.
Un comando es un programa que se puede ejecutar desde la terminal. Se le puede pasar parámetros y opciones.

## Comando
Un comando puede ser:
1. Un programa ejecutable compilado en algún lenguaje de programación. Suelen estar en /usr/bin/
2. Un comando de utilidad shell. Es una función de la shell que viene por defecto.
3. Una función de shell externa a la shell.
4. Un alias.

El comando type muestra la naturaleza de los comandos.

- https://platzi.com/blog/41-comandos-terminal/

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

## Compresión de archivos
El comando tar con las opciones -cvf (compress, verbose [ver en la terminal lo que está ocurriendo], file), más el nombre de salida y ruta del archivo, comprime los archivos en un archivo tar

    tar -cvf ToCompress.tar ToCompress/

Para comprimir con gzip (un algoritmo de compresión muy eficiente) se añade z a las opciones y la extensión en el archivo de salida

    tar -cvzf Tocompress.tar.gz ToCompress/

Para decomprimir un archivo tar con gzip usaremos las opciones -xvfz y por parámetro el archivo y para tar -xvf y por parámetro el archivo

    tar -xvf ToCompres.tar

Para ver dentro de un archivo tar sin descomprimir se usa la opción t

    tar tvf file.tar

Para comprimir con zip se usa la opción r (recursively)

    zip -r ToCompres.zip ToCompress/

Para descomprimir se usa el comando unzip

    unzip ToCompress.zip

## Manejo de procesos
Para ver los procesos activos en la terminal

    ps ax
    top
    htop

Para terminalos los procesos

    kill PID
    kill -9 PID
    pkill -9 PNAME
    killall -9 PID/PNAME

El el programa top:
    - La opción h muestra la ayuda
    - La opción q sale de la pantalla actual
    - La opción u filtra por usuario

## Procesos en segundo plano

El comando cat puede generar un pequeño editor de texto

    cat > file.txt

Para guardar y salir se usa el comando Ctrl + d
Para dejar el edito en segundo plano se usa el comando Ctrl + z

El comando jobs muestra los procesos en segundo plano

    jobs
    [n]+ Stopped            cat > file.txt

El comando fg (foreground) trae el proceso al primer plano

    fg #

El operador de control & al final de un comando envía el proceso directamente al segundo plano

    cat > file.txt &

Para enviar un proceso al segundo plano

    bg %n

Primero se suspende el proceso con Ctrl + z
Luego se ejecuta el comando bg #
El proceso se sigue ejecutando en segundo plano y se puede seguir usando la terminal

## Editores de texto en la terminal
-vim https://www.vim.org/docs.php
-Emacs https://www.gnu.org/software/emacs/
-nano https://www.nano-editor.org/

## VIM
El comando vim ejecuta el editor de texto vim (vi improved), una versión moderna de vi

Para salir de vim

    :q + Enter

Para crear un archivo de texto

    vim index.html

Para entrar en modo insert (editar)

    i

Para salir del modo insert pulsar la tecla Esc

Para buscar caracteres en el editor

    /caracteres + Enter

Para eliminar líneas enteras
    -Modo normal
    -Cursor en una línea
    -dd

Para guardar un archivo
    -Modo normal
    -:w + Enter

Para guardar y salir

    :wq + Enter

Para forzar la salida si se resiste

    :wq!

## Personalizar el emulador de terminal Tilix
Instalar la terminar tilix

    sudo apt install tilix

Instalar shell zsh

    sudo apt instal zsh

Cambiar shell por defecto
$() envía un comando como parámetro

    chsh -s $(which zsh)


Al abrir la terminal

    0

oh-my-zsh
- https://ohmyz.sh/#install

    sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

Para cambiar entre terminales

    exec bash
    exec zsh

Instalar powerlevel

- https://github.com/romkatv/powerlevel10k#oh-my-zsh

    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

Set zsh en .zshrc
    ZSH_THEME="powerlevel10k/powerlevel10k"

Configurar ohmyzsh

    p10k configure

Eliminar tilix

    sudo dpkg -r tilix
    sudo apt-get remove tilix
    sudo apt-get purge tilix
    sudo apt remove tilix
    sudo apt purge tilix

Instalar programa de fuentes Ubuntu

    sudo apt install font-manager

Instalar las preferencias del sistema Ubuntu

    sudo apt install gnome-control-center

## Libros
### Terminal
- Linux basics for hackers
- The linux command line

### Búsqueda
- Grep - O'Reilly
- Regular Expresion - O'Reilly

### Linux
- Linux - O'Reilly
- vi and Vim Editors - O'Reilly

## Wildcards

Caracteres que terminen por
     ls *.ext

Caracteres que empiecen por
     ls caracteres*

Caracteres que empiecen por mayúscula
     ls [[:upper:]]*

Directorios que empiecen por mayúscula
     ls -d [[:upper:]]*

Directorios que empiecen por minúscula
     ls -d [[:lower:]]*

Búsqueda por caracteres que empiecen por 'a' e 'i'
     ls -d [ai]*

Búsqueda por rango de números
    ls nombre[4-6]*

Búsqueda por cantidad de caracteres
    ls -l nombre??.jpg

- https://platzi.com/clases/2292-terminal/37346-wildcards/

Ver la información de una sesión

    pip install session-info
    import session_info
    session_info.show()

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

whatis -> muestra un descripción corta de un comando

## sudo
Para evitar poner la contraseña de superuser todo el tiempo
- https://www.flopy.es/evitar-que-el-comando-sudo-nos-pida-la-contrasena-en-gnu-linux/

### commands

ssh

shred --flag nombre-del-archivo -> el archivo se sobreescribe para que sea irrecuperable

rmdir -> elimina un directorio

ln -s nombre_de_un_archivo nombre-> crea un link a un archivo

    - https://www.youtube.com/watch?v=gd7BXuUQ91w