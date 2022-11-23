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

## Jupyter notebooks desde VSCode y la terminal
Mostrar la información de Conda
    conda info

Crear un jupyter notebook retornará un enlace para el navegador

    jupyter-notebook
    o: http://localhost:8888/tree#notebooks

Trabajar con notebooks desde VSCode
- Abrir VSCode desde WSL
- Instalar la extensión de Python (si no está instalada)
- Abrir un archivo jypiter notebook
- Cambiar el kernel a: base (Python #.#.#) anaconda3/bin/python [o ambiente creado]

## Ambientes con Conda
Listar los ambientes instalados en el sistema
    conda env list

Para crear un nuevo ambiente se ejecuta el comando conda create. La opcion name agrega un nombre. Si no se especifica una versión se instalará la última disponible.
    conda create --name py35 python=3.5 pandas

Para activar un ambiente se usa el comando activate seguido del nombre del ambiente
    conda activate py35

Para desactivar un ambiente se ejecuta el comando deactivate
    conda deactivate

El comando conda list muestra una lista de todos los paquetes instalados en el ambiente
    conda list

Para buscar información de un paquete en específico se ejecuta el comando list seguido del nombre del paquete
    conda list pandas

Para actualizar un paquete específio se ejecuta el comando update seguido del nombre del paquete
    conda update pandas

Para instalar una versión distinta de un paquete se ejecuta el comando install seguido del nombre del paquete y la versión
    conda install pandas=1.2

- IMPORTANTE: instalar una versión distinta de un paquete puede ocasionar incompatibilidades. Si existen la instalación falla. Para solucionarlas, Conda, devuelve un mensaje con las compatibilidades. Se instala nuevamente los paquetes con las versiones compatibles.
    conda install python=3.9 pandas=1.2

Para clonar un ambiente se ejecuta el comando conda create con las opciones name copy y clone
    conda create --name py39 --copy --clone py35

Para desinstalar una librería se usa el comando remove seguido del nombre de la librería
    conda remove pandas

Para eliminar una entorno se usa el comando env remove seguido de la opción nombre y el nombre del ambiente
    conda env remove --name py35

- No se puede eliminar un entorne que está activado (que se está usando)

## Comandos con Conda
- Importante: es una buena práctica no modificar el ambiente base

Cuando Conda no tiene información sobre un paquete que se le pide instalar se puede buscar un canal que si lo tenga en el buscador de https://anaconda.org/

Para instalar un paquete desde un canal se ejecuta el comando install con la opción channel y el nombre del paquete
    conda install --channel conda-forge boltons

Cada vez que se modifica una librería el ambiente genera revisiones. Estas son un tracking del estado del ambiente y se pueden usar para volver en el tiempo.

Para consultar las revisiones de un ambiente se ejecuta el comando list con el flag --revision
    conda list --revision

Para volver en el tiempo se ejecuta el comando install seguido del flag revision y el número de revisión
    conda install --revision 0

Para exportar un ambiente se ejecuta el comando env seguido de export. Esta ejecución genera un archivo.
    conda env export

Para exportar un ambiente solo con los nombres y versiones y paquetes se ejecuta el comando env export --no-buils
    conda env export --no-build

Para exportar un ambiente solo con los paquetes instalados manualmente se ejecuta el comando env export --from-history
    conda env export --from-history

Para exportar un ambiente a un archivo se ejecuta el comando env export con el flag --file seguido del nombre del archivo. Una extensión habitual es .yml
    conda env export --from-history --file py39.yml

Para instalar un ambiente desde un archivo se ejecuta el comando create seguido del flag file y el nombre del archivo
    conda env create --file py39.yml

Desactivar el inicio acutomático del entorno base de conda
    conda config --set auto_activate_base false

## Mamba
Mamba es un reimplementation de conda en C++ diseñada para acelerar los procesos.

- https://mamba.readthedocs.io/en/latest/

Instalar Mamba desde cero con miniforge
- https://mamba.readthedocs.io/en/latest/installation.html
- https://github.com/conda-forge/miniforge#mambaforge
    wget "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh" bash Mambaforge-$(uname)-$(uname -m).sh

Instalar Mamba desde la terminal
    conda install mamba -n base -c conda-forge

Mostrar la ayuda de Mamba
    mamba --help

Instalar librerías con Mamba
    mamba create -n nameofmyenv <list of packages>

## Divide y vencerás
Separar un problema en partes pequeñas y resolverlas individualmente

Aplicando esta técnica a los entornos evita problemas de compatibilidades cuando se generan actualizaciones.

Se recomienda trabajar con varios entornos de trabajo en mismo proyecto, cada uno separado por ambientes externos, ambientes modelo y ambiente comunicación
- proyecto_01
    - data
    - models
    - notebooks
    - envs
        - external.yml
        - model.yml
        - comunication.yml

Snakemake es un motor de flujo de trabajo que permite ejecutar un entorno distinto según la etapa en la que se encuentre
