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
Son funciones pueden recibir como argumentos otras funciones

## Módulos
Un módulo es un fichero con la extensión .py que contiene funciones, clases o variables.

### Acceso a un módulo

- Declaración import
- Ejecución como script por consola

Cuando se accede a un módulo desde otro módulo, al ejecutar el primero como script, si el segundo contiene ejecuciones también se ejecutarán.

Para evitar este comportamiento dual se declara el punto de entrada con ejecución.

    def run():
        # content
    if __name__ == '__main__':
        run()

## Paquetes
Un paquete es un directorio que contiene módulos

Antes de la versión 3.3 de Python era obligatorio crear el archivo init para que Python reconozca el directorio como paquete.


    __init__.py


En este archivo también se puede importar los módulos del paquete para que puedan ser usados directamente desde el archivo desde donde se importa el paquete.

## Data science
https://www.kaggle.com/