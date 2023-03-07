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

## Componentes
Un componente se define con una función y retorna una etiqueta con sus atributos al ser renderizado. Admite props o atributos como argumentos. Se define en un módulo de javascript (export default Componente). Se nombra con mayúscula por convención. A partir de React 17 se puede usar usar la extensión .js en lugar de .jsx.

Para trabajar con componentes dentro de otros componentes se usa la sintaxis <ComponenteHijo /> para compontes únicos o <ComponentePadre><ComponentePadre /> para componentes que van a admitir anidación.

Para que un componente admita anidación se declara un objecto children dentro de la función de creación del componete.

    const ComponentePadre = ({children}) => {
        return (<div>{children}</div>)
    }