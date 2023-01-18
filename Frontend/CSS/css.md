## Pseudoclases
Se aplican a los selectores y especifican el comportamiento de un estado.
- :active
- :focus
- :hover
- :nth-child(n)

## Pseudoelementos
Se aplican a los selectores y modifican una parte concreta del documento
- ::after
- ::before
- ::first-letter
- ::placeholder

## Arquitecturas
### Objetivos
- Ser predecible
- Reutilizable
- Mantenible
- Escalable

### Buenas prácticas
- Lineamientos
- Documentación
- Estándares
- Componenetes

### Apendix
- https://www.frontendmentor.io/

## Slider con elemento que se centre al pasar por el centro
    selector contenedor {
        display: flex;
        overflow-x: scroll;
        overscroll-behavior-x: contain;
        scroll-snap-type: x proximity;
    }
    selector elemento {
        scroll-snap-align: center;
    }

## Compatibilidad
- https://caniuse.com/