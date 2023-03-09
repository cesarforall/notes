# Atomic Design

Atomic Design es un patrón de diseño de producto el cual separa los componentes según su funcionamiento. Empezando por partes pequeñas, uniéndo se con otras para formar otras más grades y finalmente creando un todo.

- Átomos. Son componentes solo como label, input y button. Por sí solos tienen poco sentido
- Moléculas. Las moléculas son formadas por átomos y tienen una función en conjunto. Por ejemplo, juntando un label, input y button podemos formar un buscador.
- Organismos. Los organismos se forman con varias moléculas para formar un conjunto más específico. Por ejemplo, un organismo buscador se puede juntar con un organismo nav y un logo para formar un header.
- Templates. Los templates son una estructura básica con varios elementos que pueden funcionar en conjunto y ser la base útil de una página.
- Páginas. Las páginas son los templates con contenido.