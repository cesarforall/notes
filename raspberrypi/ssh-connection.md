## Configurar SSH
- https://www.raspberrypi.com/documentation/computers/remote-access.html

Abrir la configuración de raspberry

    sudo raspi-config

Entrar en:

    Interfacing Options

Seleccionar y dar ok en:

    SSH

## Cambiar contraseña y hostname

Cambiar contraseña en:

    System Options
    Password

También se puede cambiar el nombre host en:

    System Options
    Hostname

## Entrar desde VSCode
Instalar Remote - SSH (Microsoft)

Abrir una ventana nueva

Abrir Command Palette con Ctrl + Shift + P

Buscar SSH

Connect current window to host

Añadir raspberrypi.local

Logerarse con user@raspberrypi

Introducir la contraseña