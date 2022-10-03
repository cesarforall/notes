# Conceptos

## Mutable and immutable

Mutable significa modificar un dato de una variable. Esta práctica puede causar efectos colaterales si el código utiliza la variable en distintas funciones a lo largo del código.

Para prevenir los efectos colaterales y, además, no duplicar el peso de los datos, se aplica la inmutabilidad en JavasScrip.

La inmutabilidad se aplica creando la nueva variable con la estructura de datos usando la misma refencia en memoria de los datos no modificados.

## División de responsabilidades

El código y algoritmos se realizan por pasos. Primero se generan los datos y luego se representan. Es más eficiente que ir representando cada dato según se va generando. Por ejemplo, al realizar un programa que cree elementos html, primero se haría un ciclo que crearía la variable de elementos y luego se haría otro ciclo pare dibujarlos.

