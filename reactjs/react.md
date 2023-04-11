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

## react-routes-dom

React Routes DOM maneja rutas en aplicaciones para el navegador.

A partir de v6 se hacen algunos cambios:

- Switch -> Routes
- component -> element
- {Componente} -> {<Componente/>}

Dependiendo del entorno de ejecución (navegador, servidor, etc) se usará un componente distinto para envolver las rutas. En el caso del navegador se envuelve la ruta con el componente <BrowserRouter><BrowserRouter/>

En el caso de una versión de react-router-dom anterior a v6, las rutas se declaran en los componentes <Route/> con los atributos exact path='/endpoint' y component={Componente}

    <Route exact path='/endpoint' component={Component} / >

Para manejar una página no encontrada se usará el mismo componente Route con solo el atributo component={Componente}

    <Route component={Pagina404} / >

Para manejar una terminación exacta de endpoint en todas las rutas se usa el componente <Switch><Switch/> para envolver todas las rutas

    import {BrowserRouter, Switch, Route} from 'react-router-dom';
    import Componente from '../components/Componente';
    import Pagina404 from '../pages/Pagina404';

    <BrowserRouter>
        <Switch>
            <Route exact path='/' component={Componente}>
            <Route component={Componente}>
        <Switch/>
    <BrowserRouter/>

Para usar el código anterior desde react-router-dom v6 se harán los siguientes cambios:

    import {BrowserRouter, Routes, Route} from 'react-router-dom';
    import Componente from '../components/Componente';
    import Pagina404 from '../pages/Pagina404';

    <BrowserRouter>
        <Routes>
            <Route path='/' element={<Componente/>}>
            <Route path='*' element={<Pagina404/>}>
        <Routes/>
    <BrowserRouter/>

Atención! En unas primeras pruebas no me funcionó con React17.

## Stateful vs. Stateless Components

Dentro de React existen dos tipos de componentes, los smart o statefull, y los silly o stateless components.

Los stateless components son componentes funcionales (se declaran con una función y reciben props).

    import React from 'react';

    function Componente(props) {
        return (
            <p>${props.example}</p>
        )
    }

Los statefull components son componentes de clase, tienen como método obligatorio el render. Su comportamiento tiene un ciclo de vida.

    import React from 'react';

    class Component extends React.Component {
        render() {
            return <h1></h1>
        }
    }

    import React, {Component} from 'react';

    class Component extends Component {
        render() {
            return <h1></h1>
        }
    }

El uso del método constructor y el state dentro del mismo han cambiado con la sintaxis de javascript moderno y la salida de los hooks.

    import React from 'react';

    class Component extends React.Component {
        constructor(props) {
            super(props);
            this.state = {counter: 0};
            this.handleClick = this.handleClick.bind(this);
        }
        handleClick(){
            // ...
        }
        render(){
            <>
                <p>{this.state.counter}</p>
            </p>
        }
    }

## Elemento vs Componente

Un componente es una función que al ejecutarla devueleve un elemento

Un elemento es lo que devuelve la función y que es renderizado po React

## Props

Las props o propiedades se reciben como parámetros en la función que crea el componente y los argumentos se envían en el elemento como si fueran atributos html

    export function TwitterFollowCard({ name, userName, isFollowing }) {
        console.log(`${name} is following: ${isFollowing}`);
        const imgSrc = `https://unavatar.io/${userName}`;
        return (
            <article className='tw-followCard'>
                <header className='tw-followCard__header'>
                    <img className='tw-followCard__avatar' src={imgSrc} alt={`El avatar de ${userName}`} />
                    <div className='tw-followCard-info'>
                        <strong>{name}</strong>
                        <span>@{userName}</span>
                    </div>
                </header>
                <aside>
                    <button>Seguir</button>
                </aside>
            </article>
        );
    }

    import './App.css';
    import { TwitterFollowCard } from './components/TwitterFollowCard';

    export function App() {
        return (
            <div style={{ width: '320px' }}>
                <TwitterFollowCard isFollowing name='César Almeida Reyes' userName='cesarforall' />
                <TwitterFollowCard isFollowing={false} name='Miguel Ángel Durán' userName='midudev' />
            </div>
        );
    }

Importante, las props se pueden enviar como un objecto aunque es mala práctica

    export function TwitterFollowCard({ name, userName, isFollowing }) {
    console.log(`${name} is following: ${isFollowing}`);
    const imgSrc = `https://unavatar.io/${userName}`;
        return (
            <article className='tw-followCard'>
                <header className='tw-followCard__header'>
                    <img className='tw-followCard__avatar' src={imgSrc} alt={`El avatar de ${userName}`} />
                    <div className='tw-followCard-info'>
                        <strong>{name}</strong>
                        <span>@{userName}</span>
                    </div>
                </header>
                <aside>
                    <button>Seguir</button>
                </aside>
            </article>
        );
    }

## Children

Para renderizar elementos dentro de otros elementos se tiene que añadir la propiedad children en el componente.

    export function TwitterFollowCard({ children, name, userName, isFollowing }) {
        console.log(`${name} is following: ${isFollowing}`);
        const imgSrc = `https://unavatar.io/${userName}`;
        return (
            <article className='tw-followCard'>
                <header className='tw-followCard__header'>
                    <img className='tw-followCard__avatar' src={imgSrc} alt={`El avatar de ${userName}`} />
                    <div className='tw-followCard-info'>
                        <strong>{name}</strong>
                        <span>@{userName}</span>
                        {children}
                    </div>
                </header>
                <aside>
                    <button>Seguir</button>
                </aside>
            </article>
        );
    }

    import './App.css';
    import { TwitterFollowCard } from './components/TwitterFollowCard';

    export function App() {
        const elonMusk = { isFollowing: false, name: 'Elon Musk', userName: 'elonmusk' };
        return (
            <div style={{ width: '320px' }}>
                <TwitterFollowCard isFollowing name='César Almeida Reyes' userName='cesarforall' />
                <TwitterFollowCard>
                    <h1>Hello h1</h1>
                </TwitterFollowCard>
                <TwitterFollowCard isFollowing={false} name='Miguel Ángel Durán' userName='midudev' />
                <TwitterFollowCard {...elonMusk} />
            </div>
        );
    }

## useState

useState es un hook que permite agregar la funcionalidad de almacenar un estado dentro de un componente.

Recibe un array de dos elementos. El primer elemento almacena el estado por defecto. El segundo el nuevo estado.

    const state = useState(false)
    const isFollowing = state[0]
    const setIsFollowing = state[1]

La expresión equivalente se puede hacer de forma desestructurada

    const [isFollowing, setIsFollowing] = useState(false)
