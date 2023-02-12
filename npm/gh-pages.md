# Hacer deploy desde la terminal
Importante!
Actualizar (push) el repositorio en GitHub

Instalar el paquete gh-pages al proyecto
    npm install gh-pages --save-dev

Añadir el script deploy a con la ruta del directorio de la página estática a package.json. Cuando se ha publicado con éxito muestra el mensaje 'Published'
    "deploy": "gh-pages -d src"

Ejecutar el comando
    npm run deploy