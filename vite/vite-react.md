# Configuración de Vite para React
Instalar

    npm install react react-dom @types/react @types/react-dom vite-plugin-react --save-dev

- react y react-dom son las dependencias principales de React.
- @types/react y @types/react-dom son las definiciones de tipos TypeScript para React.
- vite-plugin-react es un plugin que permite a Vite procesar archivos de React.

Crear un archivo llamado vite.config.js en la raíz de tu proyecto.

    import reactRefresh from '@vitejs/plugin-react-refresh';

    export default {
        plugins: [reactRefresh()],
    };

Agregar un archivo HTML para incluir React y React DOM:

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>My Vite React App</title>
    </head>
    <body>
        <div id="root"></div>
        <script type="module" src="/src/main.jsx"></script>
    </body>
    </html>

Crea un archivo llamado main.jsx en la carpeta src con el siguiente contenido:

    import React from 'react';
    import ReactDOM from 'react-dom';

    function App() {
    return <h1>Hello, World!</h1>;
    }

    ReactDOM.render(<App />, document.getElementById('root'));

Ejecutar el comando npm run dev para iniciar el servidor de desarrollo de Vite.