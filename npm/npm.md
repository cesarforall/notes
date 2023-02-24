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

# ejecutar comandos

La clave 'scripts' en el objeto json de package.json contiene como valor un objeto cuyo key será el alias de un comando y el value, el comando a ejecutar en la terminal.

Por defecto, npm, tiene varios comandos como npm start o npm test.

npm start ejecuta el archivo que se encuentre como valor en el key main.

Para ejecutar otros comandos que no estén por defecto se ejecutará npm run alias-definido-en-scripts.

      "scripts": {
        "start": "node src/index.js"

        }
