## Programar para Ciencia de Datos
REPL Read Evaluate Print Loop es el ciclo que usaba IPython para hacer los análisis. Con el tiempo evolucionó a Jupiter Notebooks.

Jupiter Notebooks permite documentar los análisis con un sinfín de detalles. A diferencia de un Script que es más rudimentario.

Al final del día los dos tipos se complementan.

## Notebooks
- En la nube ya tienen todas las herramientas y se puede ampliar la capacidad de los recursos
- En local hace falta instalar todas las herramientas
- En la nube tienen mejores tiempos de ejecución
- Son más escalables

## Google Colab
Es un software en la nube basado en notebooks que vive dentro de drive.

- No requiere configuración
- Trabaja a nivel archivo. El punto de entrada es un notebook.
- Uso gratuito de GPUs y TPUs

GoogleColab permite gestionar los recursos.

Shift + Enter -> cierra una celda de texto y la muestra

Para subir archivos se hace doble click en el folder de GC. Estos archivos se eliminarán automáticamente cuando nos se usen durante algún tiempo.

Ctrl + Shift + p abre la paleta de comandos

## Librerías de ciencia de datos
📊 matplotlib: Generación de gráficos a partir de listas o arrays.
🧑‍💻 numpy: Cómputo científico para la manipulación de vectores.
🧑‍💻 pandas: Manipulación y análisis de datos de tablas y series temporales.
🧑‍💻 scipy: Herramientas y algoritmos matemáticos.
📊 seaborn: Visualización de datos estadísticos.

    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import scipy as sc
    import seaborn as sns

## Deepnote
- Servicio en la nube
- Basado en jupiter notebooks
- No requiere configuración
- Trabajo a nivel proyecto
- Colaboración en tiempo real
- Integración con múltiples Apps
- Acceso a terminal comandos
- Almacenamiento de variables de entorno
- Permite publicar los proyectos

## Extensiones VSCode
- wsl
- Python. Instala Jupyter
- Magic Python
- Material icon
- Rainbow Brackets
- Remote Development

## Editor de código vs IDE
Un IDE (entorno de desarrollo integrado) se enfoca a un solo lenguaje de programación y se maneja con archivos. Tiene todas la herramientas para trabajar en proyectos dicha tecnología.

    - Visual Studio
    - Android Studio (tiene su propio emulador)
    - PyCharm

Un editor de código soporta distintos lenguajes de programación y con pluggins y extensiones puede llegar a funcionar como un ide.

    - VSCode
    - Atom
    - Sublime Text

## Virtual Environmment
Un ambiente virtual es un proyecto que puede tener sus propias dependencias, independientemente de las dependencias que puedan tener los demás proyectos alojados en la misma máquina

## Conda
Conda es un administrador de paquetes y ambientes virtuales para cualquier lenguaje de programación. Su versión completa AnaConda, a diferencia de la versión mini MiniConda, contiene todas las dependencias necesarias para trabajar con proyectos de Ciencia de Datos.

- https://www.anaconda.com/products/distribution

## Cómo instalar anaconda
1. Descargar el archivo con el comando wget
    wget -O anaconda.sh https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh

2. Ejecutar el instalador con el comando bash
    bash anaconda.sh

## Como trabajar con Conda
Mostrar la información de Conda
    conda info

Crear un jupyter notebook retornará un enlace para el navegador

    jupyter-notebook
    o: http://localhost:8888/tree#notebooks

Trabajar con notebooks desde VSCode
- Instalar la extensión de Python
- Abrir un notebook
- Cambiar el kernel a: base (Python #.#.#) anaconda3/bin/python