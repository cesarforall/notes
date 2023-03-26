const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
	entry: {
		entry: './src/entry.js',
		index: './src/index.js',
		data: './src/data/data.js',
	},
	output: {
		filename: '[name].js',
		path: path.resolve(__dirname, 'dist/script/'),
		publicPath: './',
		clean: true,
	},
	module: {
		rules: [
			{
				test: /\.html$/,
				use: 'html-loader',
			},
		],
	},
	plugins: [
		new HtmlWebpackPlugin({
			template: './src/index.html',
		}),
	],
	devServer: {
		static: {
			directory: path.join(__dirname, 'src/index.html'),
		},
		historyApiFallback: true,
	},
};
