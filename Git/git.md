## Rebase

    git rebase main
    git rebase alternative

El comando rebase se usa para añadir una rama alternativa a la historia principal de la que procede.

Para hacerlo bien primero se aplica rebase a la rama alternativa y luego a la principal

## Sobreescribir repositorio
Lo principal es usar el comando --force. Es una mala práctica y puede causar conflicto al tratarse de un repositorio ya en la nube.

    git push origin HEAD --force

## Eliminar un commit y volver a uno anterior
- https://stackoverflow.com/questions/1338728/how-do-i-delete-a-commit-from-a-branch

Estando en el último commit se especifica los que se van a borrar

git reset --hard HEAD~1

