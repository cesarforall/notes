// .forEach() es un método del objeto Array
// Ejecuta una función dada por cada elemento del array
// arr.forEach(function callback(currentValue, index, array){//tu iterador}[, thisArg]);

const letters = ['a', 'b', 'c'];

for (let index = 0; index < letters.length; index++) {
	const element = letters[index];
	console.log('for', element);
}

letters.forEach(item => {
	console.log('forEach', item);
});
