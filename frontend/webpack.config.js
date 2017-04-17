const path = require('path');
const webpack = require('webpack');

module.exports = {
	entry: './src/index',
	output: {
		filename: 'scripts.js',
		path: path.join(__dirname, '../testsystem/static/testsystem')
	},
	cache: true,
	watchOptions: {
		aggregateTimeout: 100
	},
	watch: true,
	devtool: "cheap-inline-module-source-map",
	module: {
		loaders: [
			{
				test: /\.js$/,
				include: [
					path.join(__dirname, 'src')
				],
				loader: 'babel-loader',
				query: {
					presets: ['es2015'],
					plugins: ['transform-runtime', 'transform-object-rest-spread']
				}
			}
		]
	}
}