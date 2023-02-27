# Webpack
Webpack empaqueta los archivos de un proyecto optimizando su rendimiento. Usa un punto de entrada y entiende el grafo del proyecto. Usa loaders y plugins para entender el código.

## Instalar webpack
npm install webpack -> instala webpack en el proyecto actual

## Ejecutar webpack
npx webpack -> ejecuta webpack y crea el archivo main.js en dist/ por defecto. Usa los archivos que se encuentren en el directori src/

npx webpack --mode development -> ejecuta webpack y crea un archivo main.js con comentarios y formato para debuggear por el desarrollador

npx webpack --mode production -> ejecuta webpack y crea un archivo main.js para enviarlo a producción