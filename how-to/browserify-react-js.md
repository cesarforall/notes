## Aplicación ReactJS sin server
## Init
Crear archivo json con npm
    npm init
    
    {
        "name": "lab-tools-app",
        "version": "1.0.0",
        "description": "",
        "main": "index.js",
        "scripts": {
            "build": "browserify src/index.js -o build/app.js -t [ babelify --presets [ @babel/preset-env @babel/preset-react ] --plugins [ babel-plugin-transform-class-properties ] ]"
        },
        "author": "César Almeida <tankecode@gmail.com>",
        "license": "MIT",
        "devDependencies": {
            "@babel/core": "^7.9.6",
            "@babel/preset-env": "^7.9.6",
            "@babel/preset-react": "^7.9.4",
            "babel-plugin-transform-class-properties": "^6.24.1",
            "babelify": "^10.0.0"
        },
        "dependencies": {
            "browserify": "^17.0.0",
            "create-react-class": "^15.6.3",
            "react": "^16.13.1",
            "react-dom": "^16.13.1",
            "react-json-view": "^1.19.1"
        }
    }

Instalar las dependencias

    npm install

Instalar browserify

    npm install browserify

Crear las estructura de directorios

    - build
    - src
    - index.html

Crear la estructura de index.html

    <!DOCTYPE html>
    <html lang="es">
        <head>
            <meta charset="UTF-8" />
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Document</title>
        </head>
        <body>
            <div id="app"></div>
            <script src="build/app.js"></script>
        </body>
    </html>

Construir la aplicación

    npm run build