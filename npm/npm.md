# npm

npm (Node Package Manager) es el gestor de paquetes que se creo para Node.

npm init -> ejecuta la herramienta para crear package.json
npm init -y -> instala la configuración por defecto
npm help init -> descripción del funcionamiento de los campos de npm init

npm install nombre-del-paquete || npm install nombre-del-paquete --save || npm install nombre-del-paquete -S -> instala un paquete y lo guarda como dependencia
"dependencies": {
"moment": "^2.29.4"
}

npm install nombre-del-paquete --save-dev || npm install nombre-del-paquete --D -> instala un paquete y lo guarda como dependencia de desarrollo
"devDependencies": {
"eslint": "^8.34.0"
}

npm install -g nombre-del-paquete -> instala un paquete de forma global sin afectar y no afecta al package.json actual
npm install nombre-del-paquete -o -> instala un paquete de forma opcional

Si se ejecuta el comando npm install con el nombre de una dependencia ya instalada y un flag distinto al que se instaló previamente, la dependencia se actualizará

npm list -> muestra los paquetes instalados
npm list -g -> muestra los paquetes instalados de forma global

npm install -nombre-del-paquete --dry-run -> hace una simulación de instalación. Se usa para comprobar si habrá conflictos al instalar distintas versiones de un mismo paquete

npm install -nombre-del-paquete@0.0.0 -> instala una versión específica de un paquete

npm install -nombre-del-paquete@latest -> instala la versión más actual de un paquete

npm install -> instala los paquetes que estén declarados en package.json

##
Cambiar la configuración defecto globalmente
    npm config set <Key> <Value> -g

Cambiar el autor por defecto
    npm config set init-author-email "cesaralmeida89@gmail.com" -g

Cambiar la configuración por defecto
    npm config set init-author-name "César Almeida" -g
    npm config set init-author-url "https://github.com/cesarforall" -g
    npm config set init-license "MIT" -g


# ejecutar comandos

La clave 'scripts' en el objeto json de package.json contiene como valor un objeto cuyo key será el alias de un comando y el value, el comando a ejecutar en la terminal.

Por defecto, npm, tiene varios comandos como npm start o npm test.

npm start ejecuta el archivo que se encuentre como valor en el key main.

Para ejecutar otros comandos que no estén por defecto se ejecutará npm run alias-definido-en-scripts.

      "scripts": {
        "start": "node src/index.js"

        }

# npx

npx (Node package execute) ejecuta directamente los paquetes sin tener que instalarlos previamente ni hacer una instancia de los mismos.

## Trabajar con otros proyectos
Instalar las dependencias de un proyecto ya desarrollado puede generar varios conflictos:

npm outdate muestra en pantalla una tabla con las versiónes del proyecto, las requeridas por el mismo y las más actuales en el gestor de paquetes.

### Peer dependencies
Peer dependencies expresa la compatibilidad de una dependencia con el proyecto o dependencia. Para ello se especifica una versión o versión base desde la que se puede trabajar en el proyecto.

  {
    "name": "tea-latte",
    "version": "1.3.5",
    "peerDependencies": {
      "tea": "2.x"
    }
  } 

Al hacer la instalación, si la peer dependency no está actualizada, el programa muestra un warning.

Se soluciona instalando la versión correcta de la dependencia.

### Vulnerabilities
- Low
- Moderate
- High
- Critical

## Resolver conflictos
npm audit muestra en pantalla los conflictos de dependencias en los proyectos.

npm audit fix resuelve algunos conflictos
npm audit fix --force resuelve más conflictos todavía

Ejecutar la instalación más reciente de un paquete que sigue teniendo conflictos puede resolver el conflicto

## Eliminar dependencias
npm uninstall nombre-de-la-dependencia elimina una dependencia del proyecto.

También se puede eliminar la key value de la dependencia en package.json, eliminar la campeta node_modules e intalar todo de nuevo. Esta forma de hacerlo limpia el proyecto como añadido

rm -rf node_modules
npm install

## Instalacion limpia
npm ci instala las dependencias de una forma limpia
Requiere que exista un package-lock.json en el proyecto o si no devolverá un error
Si se usa en lugar de install se debe proveer de los flags igual que si se usase install
Se usa en entornos automatizados o de integración continua. No sobreescribe package.json ni package-lock.json, no los sincroniza. Se limita a instalar lo que está declarado.

## Comandos adicionales
npm [comando] --dd muestra todo el proceso del comando en pantalla

Crear en comando en package.json para que haga todo el proceso:
json // package.json { "scripts": { "phoenix": "rm -f package-lock.json && rm -rf ./node_modules && npm i --no-fund --no-audit" } }

## Publicar paquetes
El nombre del repositorio debe ser el mismo que el del paquete, por lo tanto, antes de crear el repositorio se hará una búsqueda por nombre del paquete en npmjs.com.

npm link instala de forma global el paquete actual

npm install ruta/del/directorio instala el paquete en el directorio actual

npm adduser agrega el usuario de npmjs.com

npm publish publica el paquete

## Actualizar paquetes
Para actualizar paquetes el repositorio debe estar actualizado y subido, es decir, limpio.
La versión al actualizar el paquete debe ser distinta que la anterior o npm devolverá un error.
npm version 0.0.0 cambia la versión de un paquete o proyecto y hace un commit.
npm pusblish publica la última versión del proyecto.