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