# Babel js

Babel es un compilador (transpilador) de javascript. Transforma el código moderno a uno antiguo para que lo entiendan navegadores con versiones más antiguas de javascript.

## Usar Babel desde Node

Instalar @babel/core y babel-cli como dependencia
npm install @babel/core babel-cli

Crear un archivo .babelrc con un objeto con la configuración de presets plugins

    {
        presets: ["es2015", "@babel/preset-env"],
        plugins: ["@babel/plugin-transform-runtime"]
    }

