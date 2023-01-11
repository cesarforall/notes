# Javascript
## Qué es Javascript
Es el lenguaje de programación que entiende el navegador y permite que las páginas web se conviertan en dinámicas o aplicaciones web.

Como lenguaje de programación es:
- Alto nivel. Su sintaxis es cercana al entendimiento humano.
- Interpretado. El ordenador lee línea por línea el código en el runtime
- Orientado a objetos. Parte de objetos como base.
- Débilmente tipado. No se especifica el tipo de datos y Javascript los intenta interpretar
- Dinámico. Se puede ver el resultado directamente en el navegador sin esperar a que pase por una etapa completa de compilación

## Cómo funciona Javascript en el navegador
- El navegador obtiene el código
- El motor de Javascript (V8 en Chrome) genera un árbol de palabras clave en JS y lo traduce a código binario en un proceso llamado JIT (Compiler)
- El motor de JS se comunica con el ordenador

## Backwards y Forwards
Las nuevas versiones de JS no se pueden usar en entornos antiguos. Para hacer JS backward compatible usa el compilador Babel que traduce lo nuevo a lo antiguo.

## Mutable and immutable

Mutable significa modificar un dato de una variable. Esta práctica puede causar efectos colaterales si el código utiliza la variable en distintas funciones a lo largo del código.

Para prevenir los efectos colaterales y, además, no duplicar el peso de los datos, se aplica la inmutabilidad en JavasScrip.

La inmutabilidad se aplica creando la nueva variable con la estructura de datos usando la misma refencia en memoria de los datos no modificados.

## División de responsabilidades

El código y algoritmos se realizan por pasos. Primero se generan los datos y luego se representan. Es más eficiente que ir representando cada dato según se va generando. Por ejemplo, al realizar un programa que cree elementos html, primero se haría un ciclo que crearía la variable de elementos y luego se haría otro ciclo pare dibujarlos.

## Variables
Una variable es la representación de algún lugar en memoria que se va a usar para guardar un valor