Base de un proyecto con React
Crear el directorio src con index.js

    src
        index.js

    index.js

    import React from 'react';
    import ReactDOM from 'react-dom';
    import App from './components/App';

    ReactDOM.render(<App />, document.getElementById('app'));

Crear el directorio componentes dentro de src con el componente App

    src
        components
            App.jsx

    App.jsx

    import React from 'react';

    const App = () => <h1>Hello React!</h1>;

    export default App;

Crear el directorio public en la raiz con index.html

    public

        index.html

    <DOCTYPE! html>
    <html lang='en'>
        <head>
            <meta charset='UTF-8'>
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Webpack React<title>
        </head>
        <body>
            <div id='app'></div>
        </body>
    </html>

## Trabajndo con html

    npm install html-loader html-webpack-plugin -D

html-loader permite a webpack entender los archivos html. Se configura añadiendo una regla con el test: /\.html$/, loader: 'html-loader'.

html-webpack-plugin crea un archivo html para dist a partir de un template (publc/index.html)

## Trabajar con css

    npm install mini-css-extract-plugin css-loader style-loader sass sass-loader -D

css-loader recolecta todo el css de la aplicación y lo convierte a un string

style-loader injecta el string que el css loader ha generado y lo inyenta en etiquetas style en el bundle.

sass-loader carga archivos sass y los compila en css

mini-css-extract-plugin extrae css de archivos separados y lo junta para servirlo como uno solo para servirlo donde se le requiere

## Preparar el proyecto para producción

    npm install css-minimizer-webpack-plugin terser-webpack-plugin clean-webpack-plugin -D

Añadir las configuraciones en webpack.config.js

    const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');
    const TerserPlugin = require('terser-webpack-plugin');
    const { CleanWebpackPlugin } = require('clean-webpack-plugin');

Añadir publicPath en output

    	output: {
    	path: path.resolve(__dirname, 'dist'),
    	filename: 'bundle.js',
    	publicPath: '/',
        },

Añadir los plugin

    	plugins: [
    	new HtmlWebpackPlugin({
    		template: './public/index.html',
    		filename: './index.html',
    	}),
    	new MiniCssExtractPlugin({
    		filename: '[name].css',
    	}),
    	new CleanWebpackPlugin(),
    ],

Añadir optimization

    optimization: {
    	minimize: true,
    	minimizer: [new CssMinimizerPlugin(), new TerserPlugin()],
    },
