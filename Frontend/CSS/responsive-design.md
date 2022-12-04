# Responsive Design
## Viewport
Es el área donde se presenta la información

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

## Media Queries
Controlan el comportamiento de de los estilos según el tamaño de pantalla

    @media (min-width: 600px) {
        body {
            background-color: red;
        }
    }
    @media (max-width: 599px) {
        body {
            background-color: blue;
        }
    }

## Flexbox
La propiedad flexbox permite organizar los elementos internos en conjunto