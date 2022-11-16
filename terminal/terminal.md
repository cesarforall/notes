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