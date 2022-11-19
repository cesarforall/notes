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

    ls; mkdir dir; cal

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

## Cómo modificar permisos en la terminal

Con el usuario root activo (ejecutar sudo su)

    chmod 000 file.ext