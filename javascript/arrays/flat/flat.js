// El método flat devuelve un array simplificado de varios arrays anidados

const matrix = [
	[1, 2, 3],
	[4, 5, 6, [7, 8, [9, 10, 11]]],
	[12, 13, 14],
];

const newArray = [];
for (let i = 0; i < matrix.length; i++) {
	const array = matrix[i];
	for (let j = 0; j < array.length; j++) {
		const element = matrix[i][j];
		newArray.push(element);
	}
}
console.log('for', newArray);

const rta = matrix.flat();
console.log('flat', rta);

// Para bajar a niveles inferiores le pasamos un número como argumento
const rta2 = matrix.flat(3);
console.log('flat', rta2);

// Challenge - Simplificar un array de distintos niveles con recursión

const flatten = arr => {
	return arr.reduce((previousValue, currentValue) => {
		return previousValue.concat(Array.isArray(currentValue) ? flatten(currentValue) : currentValue);
	}, []);
};

console.log('flatten', flatten(matrix));
