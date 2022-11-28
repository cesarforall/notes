## NumPy
Es una librería para el cálculo numérico y manipulación de arrays
- Nace en 2005
- Open source
- Muy veloz
- Optimiza el almacenamiento en memoria
- Maneja mucho tipos de datos
- Solo con NumPy se ha llegado ha construir redes neuronales

        import numpy as np

### Array
Es la estructura central de NumPy, representa datos de manera estructurada, sus elementos están indexados y son de fácil acceso.

    import numpy as np

    a = np.array([1, 2, 3])

## Dimensionses
### Scalar
    Un solo dato. No tiene dimensiones. Por ejemplo una celda de excel
    []
### Vector
    Una lista de datos. Por ejemplo una fila de datos
    [][][][][]
    
    []
    []
    []
    []
    []
### Matrix
    Por ejemplo una tabla con filas y columnas
    [][][][][]
    [][][][][]
    [][][][][]
    [][][][][]

### Tensor 3D
    Una matrix con cambios en el tiempo
    [][][][][] [][][][][] [][][][][] [][][][][]
    [][][][][] [][][][][] [][][][][] [][][][][]
    [][][][][] [][][][][] [][][][][] [][][][][]
    [][][][][] [][][][][] [][][][][] [][][][][]
### Tensor 4D
    Varios canales para un ejemplo y este se añade en el tiempo
    [][] [][] [][]      [][] [][] [][]      [][] [][] [][]
    [][] [][] [][]      [][] [][] [][]      [][] [][] [][]