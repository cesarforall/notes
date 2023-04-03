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

## Uso de logs
Los logs son el registro de cada commit.
Se organizan en una lista ordenada y se accede a ella con el comando:

    git log

Para acceder al estado del proyecto en un log se usa el string de la identificación del commit y el comando:

    git checkout id-del-commit

    Note: switching to 'id-del-commit'.

    You are in 'detached HEAD' state. You can look around, make experimental
    changes and commit them, and you can discard any commits you make in this
    state without impacting any branches by switching back to a branch.

    If you want to create a new branch to retain commits you create, you may
    do so (now or later) by using -c with the switch command. Example:

    git switch -c <new-branch-name>

    Or undo this operation with:

    git switch -

    Turn off this advice by setting config variable advice.detachedHead to false

    HEAD is now at id-del-commit texto-del-commit

Se puede realizar cualquier acción, incluso commits, dentro del log. Sin embargo para guardar el proceso se debe crear una nueva rama. Esta se crea con el comando:

     git switch -c nombre-de-la-nueva-rama

También se puede revertir esta acción con el comando:

    git switch -

