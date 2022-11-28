# Think like a programmer - V. Anton Spraul
## Chapter 1. Strategies for Problem Solving
### The fox, the goose and the corn
- Restate the problem in a more formal manner making operations generic, or parameterized.
    1. Operation: Row the boat from one shore to the other.
    2. Operation: If the boat is empty, load an item from the shore.
    3. Operation: If the boat is not empty, unload the item to the shore.
- The correct approach to the solution is the solution.

### Sliding Tile Puzzles
- Develop a strategy.
- Don't attack the problem through trial and error.
- Experiment with a reduced version of the problem.
- Divide a problem.
- Work with a specific goal in mind.

### Sudoku
- Look for the most constrained part of the problem for eliminate choices.
- Start with the “most constrained variable”, or put another way, the variable that has the lowest number of possible values.
- Start with the part that’s obvious. If you can solve part of the problem, go ahead and do what you can.

### The Quarrasi Lock
- It is important to recognize analogies.

## General Problem-Solving Techniques
### 1. Always have a plan
- Hacer un plan aunque no vaya a salir como lo planeado.
- Un plan no es resolver el problema completo sino declarar objetivos.
- Definir objetivos intermedios para medir el progrego.

### 2. Restate the Problem
- Replantear el problema puede dar nuevas soluciones que no se ven a simple vista

### 3. Divide the Problem
- For example, a section of code that employs a series of if statements inside a while loop that is itself inside a for loop will be more difficult to write (and to read) than a section of code that employs all those same control statements sequentially.

### 4. Start with What You Know (maxim)
- Empezar con los conocimientos que ya tenemos.
- When we begin our investigation of a problem by applying the skills we already have, we may learn more about the problem and its ultimate solution.

### 5. Reduce the Problem
- Reducir el problema a partes que se puedan resolver para llegar a un entendimiento de las partes de las cuales no encontramos todavía una solución.

### 6. Look for Analogies
- Cada problema que resuelva será una potencial analogía para resolver nuevos problemas.

### 7. Experiment
- Experimentar es un proceso controlado que revela nuevas vías para resolver el probelma original.

### 8. Don't Get Frustrated
- Cambiar de actividad antes de que la frustración llegue. Esto puede ser cambiar de problema o de actividad.
- Cuando se está mucho tiempo ante el ordenador es recomendable tener una rutina de estiramientos.

## Chapter 2. Pure Puzzles
### Output Patterns

Problema: formar un triángulo o medio cuadrado con solo cout << "#" y cout << "\n"
    #####
    ####
    ###
    ##
    #

¿Cómo puedo reducir este problema a un punto fácil deresolver?
1. Un cudrado
    #####
    #####
    #####
    #####
2. Una línea
    #####

Lo resuelvo con un loop para generar la línea
    for (int hasNum = 1; hashNum <=5; hasNum++) {
        cout << "#";
    }
    cout << "\n";

    #####

Añado un loop para generar el cuadrado
    for (int row = 1; row <= 5; row++) {
        for (int hasNum = 1; hashNum <=5; hasNum++) {
            cout << "#";
        }
        cout << "\n";
    }

    #####
    #####
    #####
    #####

Es siempre más fácil trabajar la solución en aislamiento. Olvidar por un momento los hashes ayudarán a centrarnos en los números.

    for (int row = 1; row <=5; row++) {
        cout << (1) expression << "\n";
    }

|row|desired value|row*-1|difference from desired value|
|---|---|---|---|
|1|5|-1|6|
|2|4|-2|6|
|3|3|-3|6|
|4|2|-4|6|
|5|1|-5|6|
    
    for (int row = 1; row <=5; row++) {
        cout << 6 - row << "\n";
    }

Despues de encontrar la solución ya podremos implementarla

    for (int row = 1; row <= 5; row++) {
        for (int hashNum = 1; hashNum <= 6 - row; hashNum++) {
            cout << "#";
        }
        cout << "\n";
    }

Problema: formar un triángulo solo con # y \n
    #
    ##
    ###
    ##
    #

Uso la analogía de otro problema parecido y listo lo que sé del problema anterior
- Representar una fila de símbolos de un tamaño particular usando un loop
- Representar una serie de filas usando ciclos anidados
- Crear una variedad de símbolos en cada fila usando una expresión algebraica en lugar de un valor calculado
- Descubrir la expresión algebraica correcta a través de la experimentación y análisis

Después de buscar parecido se empieza a experimentar y encontrar las diferencias

    symbol = '#'
    lines = range(1, 8)
    symbolOutput = ''

    print('#'*5)
    print('')

    for line in lines:
        print('#'*(4 - abs(4 - line)))

Tracking State
- Es importante guardar los trozos de código o pequeños programas que formaron parte de una solución mayor para poder reusar el código si es posible.
- Al final todo se resume en cortar el código en partes pequeñas.