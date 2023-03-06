# Webpack

Webpack empaqueta los archivos de un proyecto optimizando su rendimiento. Usa un punto de entrada y entiende el grafo del proyecto. Usa loaders y plugins para entender el código.

## Loaders vs plugins

Los loaders permiten a webpack trabajar con extensiones o tipos de archivos que no admite por defecto.

Los plugins agregan funcionalidades nuevas webpack.

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

Se usa path.resolve(\_\_dirname, 'name') para especificar el directorio actual usando el módulo path. Este módulo actualmente ya forma parte de Node.

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

## Webpack con babel

Webpack admite a babel como módulo y lo conecta en la key module. Este admite un array y dentro se ub objeto configurando webpack.

test analiza el directorio actual en busca de módulos. Se excluye node_modules para no romper la aplicación y se declara el uso de babel-loader.

    module: {
    	rules: [
    		{
    			test: /\.m?js$/,
    			exclude: /node_modules/,
    			use: {
    				loader: 'babel-loader',
    			},
    		},
    	],
    },

La configuración que busca babel se declara en .babelrc con los presets y plugins

    {
    "presets": [
        "@babel/preset-env"
    ],
    "plugins": [
        "@babel/plugin-transform-runtime"
    ]

}

Se usa la configuración .babelrc cuando se tiene como objetivo el directorio donde está. Si es una configuración global se puede añadir en webpack.config.js

    {
    "presets": [
        "@babel/preset-env",
        [
            "@babel/preset-react",
            {
                "runtime": "automatic"
            }
        ]
    ]

}

## Instalar babel para webpack

    npm install babel-loader @babel/core @babel/preset-env @babel/plugin-transform-runtime

### babel-loader

Es el loader de babel para webpack

### @babel/core

Es la base de babel

### @babel/preset-env

Trabaja javascript moderno

### @babel/plugin-transfor-runtime

Trabaja con el asincronismo de javascript

## Webpack con html

Trabajar con html desde webpack se hace mediante el plugin html-webpoack-plugin.

Primero se require desde el archivo de configuración de webpack.

    const HtmlWebpackPlugin = require('html-webpack-plugin');

    plugins: [new HtmlWebpackPlugin({
        inject: true,
        template: './public/index.html',
        filename: 'index.html'
    })]

Luego se elimina cualquier script desde el html original porque webpack lo creará.

## Webpack con css y preprocesadores

 npm install mini-css-extract-plugin css-loader style-loader sass -D -> para instalar los paquetes necesarios

webpack.confij.css

      {
        test: /\.css|.styl$/i,
        use: [MiniCssExtractPlugin.loader,
          'css-loader',
          'stylus-loader'
        ],
      }

index.js

    import './styles/vars.styl';

vars.styl

    $color-black = red

    body
    color $color-black
