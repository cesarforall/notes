# Cómo funciona una aplicación web
El cliente hace una petición al servidor usando las reglas de la API mediante el protocolo Http. El servidor responde con los datos mediante el mismo protocolo al cliente. Este recibe los datos y los representa visualmente en el navegador.

## Flujo de desarrollo de una aplicación web
El desarrollo se realiza en el entorno local mediante un IDE (integrated development environment) o editor de texto.

Se realizan los test con el navegador a través de un servidor local (local host).

Para gestionar la historia del código se usa un sistema de control de versiones. El más popular es git.

Para que la aplicación pueda ser accedida desde cualquier lugar necesita estar en alojada en un servidor las veinticuatro horas. Esto es estar en producción.

El proceso que consiste en  enviar el codigo desde el entorno local al servidor se llama deployment (despliegue).

El despliegue de la aplicación se puede hacer directamente al servidor. Sin embargo, estas suelen necesitar un desarrollo constante. Para ello se aplica un proceso llamado CI/CD (continuous integration, continuous deployment).

CI/CD testea cada modificación en el código y si funciona bien se actualiza en el servidor.

Subimos el código a GitHub o GitLab y estos se encargan del proceso.

El servidor asigna una dirección (ip) a la aplicación. Para que sea más fácil de acceder a la dirección se asigna un nombre de dominio con un sufijo.

## Diseño

### UI Design
User interface. Diseña las formes y colores. Los programas más usados son Adobe XD, Sketch y Figma.

### UX Design
User experience. Se encarga del diseño de la mejor posición de los elementos.

## Desarrollo Frontend
Se encarga de la parte visual y la que interactúa con el usuario.

HTML es el lenguaje para crear la estructura de la web.

CSS es lenguaje para crear estilos. Tiene librerías y frameworks como Foundation, Bootstrap y Tailwind.

JavaScript es el lenguaje de programación que usa el navegador para crear interactividad. Los frameworks y librerías más importantes son React, Angular, Svelte y Vue.

## Desarrollo backend
Se encarga de la lógica de la aplicación.
- Javascript ejecutado en NodeJS
- PHP con Lavarel
- Java con Spring
- Go
- Rust
- Ruby con Ruby on Rails
- Python cons Fast API, Flask o Django

## Framework
Conjunto de librerías y reglas para contruir un producto digital.

## Librería
Conjunto de archivos de código con funcionalidades comunes que ayudan al desarrollo de software.

## API
Application Programming Interface. Sección del backend que permite la comunicación en Frontend y backend.

La comunicación se realiza mediante mensajes de ida y vuelta.

### SOAP
Simple Objetct Access Protocol. Standard de comunicación API que mueve la información en XML (Extensible Markup Language). 

### REST
Representational State Transfer. Standard de comunicación API que mueve la información en JSON (Javascript Objet Notation). Es lo mismo que un diccionario en Python.

## Http
Hypertext Transfer Protocol. Conjunto de reglas para la transferencia de datos entre cliente y servidor.

## Tipos de servidores
### Iaas
Infrastructure as a service. Se eligen los recursos (CPU, RAM, SSD) que va a necesitar la aplicación para ser distribuida. La instalación, administración y actualizaciones del sistema operativo, bases de datos, firewall, etc, está a cargo del cliente.

VPS. Virtual Private Server. Los recursos son exlusivos para la aplicación.
Shared Hosting. Se comparten recursos con otras aplicaciones.

- Amazon Web Services
- Microsoft Azure
- Digital Ocean



### Pass
Platform as a service. Se considera just deploy. El servicio provee las herramientas, como bases de datos, firewall, etc, que necesita la aplicación. No hay ecesidad de conocer los recursos (hardware) específicos del sistema.

- Google App Engine
- Firebase
- Heroku

### Iaas
Software as a service. Usa aplicaciones ya creadas y configuradas sin necesidad de usar código (no code).

- Google Docs
- Slack
- WordPress