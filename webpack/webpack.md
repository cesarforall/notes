# Webpack
Webpack empaqueta los archivos de un proyecto optimizando su rendimiento. Usa un punto de entrada y entiende el grafo del proyecto. Usa loaders y plugins para entender el código.

## Instalar webpack
npm install webpack -> instala webpack en el proyecto actual

## Ejecutar webpack
npx webpack -> ejecuta webpack y crea el archivo main.js en dist/ por defecto. Usa los archivos que se encuentren en el directori src/

npx webpack --mode development -> ejecuta webpack y crea un archivo main.js con comentarios y formato para debuggear por el desarrollador

npx webpack --mode production -> ejecuta webpack y crea un archivo main.js para enviarlo a producción

## Configurar webpack
La configuración personalizada de webpack se hace exportando un objecto con los parametros deseados desde el archivo webpack.config.js en el directorio raiz.

npx webpack --mode production --config webpack.config.js -> ejecuta webpack con el archivo de configuración personalizado.

### webpack.config.js
El archivo de configuración webpack exporta un entry, output y resolve.

    const path = require('path');

    module.exports = {
        entry: './src/index.js',
        output: {
            path: path.resolve(__dirname, 'dist'),
            filename: 'main.js'
        },
        resolve: {
            extensions: ['.js'],
        },
    };

#### entry
'entry' especifica en un string la ruta desde el archivo raíz hacia el script principal del proyecto.

    entry: './src/index.js',

#### output
'output' especifica el directorio y archivo de salida.

Se usa path.resolve(__dirname, 'name') para especificar el directorio actual usando el módulo path. Este módulo actualmente ya forma parte de Node.

Para el archivo de salida se especifica el nombre del en el key filename.

    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'main.js',
    }

### resolve
'resolve' especifica las extensiones con las que va a trabajar webpack. Se especifican en el key extensions dentro de un array.

    resolve: {
        extensions: ['.js'],
    }