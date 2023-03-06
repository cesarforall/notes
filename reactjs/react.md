# ReactJs

React es una librería javascript frontend para mostrar las vistas en un modelo de arquitectura o patrón de diseño MVC (model view controller).

## JSX

Es una sintaxis que usa javascript y XML para hacer ágil el desarrollo de componentes.

## Virtual DOM

Es una copia de real DOM que maneja React para hacer comparaciones rápidas entre sí cuando hay cambios dinámicos en la aplicación. De este forma se renderiza solo los componentes que han cambiado.

## Ciclo de vida

El ciclo de vida es el sistema que tiene React para crear, trabajar con ellos y eliminar componentes en el DOM.

## El estado en React

El lugar donde almacenamos y actualizamos dinánicamente información de la aplicación y los usuarios.

## Dependencias React

Añadir como dependencias base:

- react
- react-dom

## Dependencias Webpack y Babel en React

Las dependencias de desarrollo que se usan en React para trabajar con Webpack y Babel son:

- @babel/core
- @babel/preset-env
- @babel/preset-react. Este plugin tiene por defecto la opción runtime como classic. La otra opción es automatic y detecta automáticamente el código en jsx y lo transforma. No necesita el import de React. Esto viene de la nueva funcionalidad de React 17, el cuál no necesita crear archivos. jsx.

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

(En el caso de querer eliminar los imports) -> npx react-codemod update-react-imports

- html-loader
- html-webpack-plugin
- webpack
- webpack-cli
- webpack-dev-server
