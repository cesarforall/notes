# ¿Por qué Python?
- Más querido por la comunidad
- Lenguaje fácil de aprender
- Mejores salarios
- Análisis de datos
- Desarrollo web
- DevOps
- Machine learning
- Demanda laboral

## Herramientas para trabajar con Python
- https://replit.com/@cesarforall
- Editores de código como Visual Studio Code.
- Terminal y línea de comandos en diversos sistemas operativos.
- Jupyter Notebooks.
- Git para control de versiones.
- Entornos virtuales con PIP.
- Entornos integrados de desarrollo (IDE) como PyCharm, Visual Studio o DataSpell.

## Lists vs Tuples vs Sets
||Mutable|Ordered|Indexing / Slicing|Duplicate elements|
|---|:---:|:---:|:---:|:---:|
|List|✅|✅|✅|✅|
|Tuple|❌|✅|✅|✅|
|Set|✅|❌|❌|❌|

- List. Se puede modificar, mantiene el orden, se puede acceder a un índice concreto, permite duplicar elementos
- Tuple. La diferencia con la lsita es que no se puede modificar
- Set. Se puede modificar, no tiene orden, ni se puede acceder a los elementos por índices. Tampoco admite elementos duplicados

## Scope

- Built-in
- Global
- Enclosing
- Local

## Higher order functions
Las funciones pueden recibir como argumentos otras funciones

## Módulos
Los archivos con la extensión .py se consideran módulos. Normalmente contienen funciones con utilidades. También pueden contener variables pero es menos habitual.

Los módulos pueden ser usados de las siguientes formas:
- Importanto el módulo en sí con 'import' para acceder a las funciones o variables.
- Ejecutándolos como script con Python.

Al importar el módulo y ejecutar el script actual la lógica completa del módulo se ejecuta.

Si necesitamos que no se ejecute encapsulamos el código dentro de una función y la validamos en el condicional

    def run():
        # content
    if __name__ == '__main__':
        run()

De esta forma podemos ejecutar el módulo como script y como módulo haciendo el import

## Paquetes
Un paquete es un directorio que contiene módulos

Antes de la versión 3.3 de Python era obligatorio crear el archivo init para que Python reconozca el directorio como paquete


    __init__.py


En este archivo también se puede importar los módulos del paquete para que puedan ser usados directamente desde el archivo desde donde se importa el packete

## Data science
https://www.kaggle.com/