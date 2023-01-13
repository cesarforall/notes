# Install Node in WSL
- https://learn.microsoft.com/es-es/windows/dev-environment/javascript/nodejs-on-wsl

1. Instalar curl si no está instalado
    sudo apt-get install curl

2. Instalar nvm
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash

3. Cerrar el terminal y abrir un nuevo terminal

4. Comprobar que está instalado nvm
    command -v nvm
    -> nvm

5. Comprobar las versiones de Node
    nvm ls

6. Instalar una versión de node lts o actual
    nvm install --lts
    nvm install node

7. Comprobar la versión de Node instalada
    nvm ls