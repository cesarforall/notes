    // webpack.config.js
    module.exports = {
    // Entrada y salida de archivos
    entry: './src/index.js',
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname, 'dist'),
    },
    // Resolución de módulos
    resolve: {
        modules: ['node_modules'],
    },
    // Manejo de diferentes tipos de archivos
    module: {
        rules: [
        {
            test: /\.js$/,
            exclude: /node_modules/,
            use: {
            loader: 'babel-loader',
            },
        },
        ],
    },
    // Modo de desarrollo y producción
    mode: 'production',
    // Opciones de optimización
    optimization: {
        minimize: true,
    },
    // Integración con Babel
    resolveLoader: {
        modules: ['node_modules'],
        alias: {
        'babel-loader': require.resolve('babel-loader'),
        },
    },
    };
