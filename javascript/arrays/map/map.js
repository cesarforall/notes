// .map() es un método del objeto Array
// Crea un nuevo array con los resultados de la función llamada
// var nuevo_array = arr.map(function callback(currentValue, index, array){// Elemento devuelto de nuevo_array}[, thisArg]);


const letters = ['a', 'b', 'c'];

// const newArray = [];
// for (let index = 0; index < letters.length; index++) {
// 	const element = letters[index];
// 	newArray.push(element + '++');
// }

const newArray = letters.map(item => item + '++');
console.log('original', letters);
console.log('new', newArray);
