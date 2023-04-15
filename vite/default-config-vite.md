    // vite.config.js
    export default {
    // Procesamiento de módulos nativos de ECMAScript
    // No es necesario transpilar el código ECMAScript utilizando herramientas como Babel.
    esbuild: {
        jsxInject: `import React from 'react';`,
    },

    // Servidor de desarrollo en tiempo real
    // El servidor de desarrollo utiliza la recarga en caliente (hot reloading) para actualizar la aplicación de forma rápida y sin tener que recargar la página.
    server: {
        port: 3000,
        hmr: {
        overlay: true,
        },
    },

    // Soporte para diferentes tipos de archivos
    // Vite admite diferentes tipos de archivos como CSS, imágenes, archivos JSON, SVG y HTML.
    // Por defecto, Vite utiliza la carga dinámica (dynamic import) para cargar estos archivos de forma eficiente.
    optimizeDeps: {
        include: [
        'react',
        'react-dom',
        '@material-ui/core',
        ],
    },

    // Optimización de producción
    // Vite utiliza Rollup.js para realizar la optimización de producción.
    // Rollup.js es un empacador de módulos que permite reducir el tamaño del archivo y mejorar el rendimiento de la aplicación.
    build: {
        target: 'es2015',
        outDir: 'dist',
        rollupOptions: {
        output: {
            manualChunks: undefined,
        },
        },
    },

    // Integración con preprocesadores de CSS
    // Vite es compatible con preprocesadores de CSS como Sass, Less y Stylus, lo que permite utilizar sintaxis más avanzadas para crear hojas de estilo.
    plugins: [
        require('@material-ui/core/styles'),
        require('autoprefixer'),
        require('cssnano')({
        preset: 'default',
        }),
    ],
    }
