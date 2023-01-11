## Importar un proyecto a Github
- https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github

### Usando Git
1. Crear un nuevo repositorio en Github

2. Ejecutar git con la rama main
    git init -b main

3. Montar y hacer commit del proyecto
    git add .
    git commit -m "initial commit"

4. Añadir el origen
    git remote add origin <REMOTE_URL>
    git remote -v

5. Hacer push
    git push origin main

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

