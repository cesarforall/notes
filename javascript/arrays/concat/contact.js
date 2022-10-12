// El método concat une dos arrays generando uno nuevo
// Es inmutable

const elements = [1, 1, 2, 2];
const othersElements = [3, 3, 4, 4];

// Al copiar un array de esta forma, la referencia en memoria es la misma.
// Por lo tanto, el array original se irá modificando
// Si lo usamos en otra operación habrá cambiado
// let newArray = elements;
// for (let index = 0; index < othersElements.length; index++) {
// 	const element = othersElements[index];
// 	newArray.push(element);
//     console.log('elements', elements)
// }
// Para copiar un array sin modificar la referencia en memoria se usa spread operator
// Pasa lo mismo al duplicar objetos con el método map
let newArray = [...elements];
for (let index = 0; index < othersElements.length; index++) {
	const element = othersElements[index];
	newArray.push(element);
}
console.log('for', newArray);

const rta = elements.concat(othersElements);
console.log('concat', rta);

// Se puede unir arrays solo con spread operator

const rta2 = [...elements, ...othersElements];
console.log(rta2);

// Spread operator separa cada elemento
const rta3 = [...elements, 'random'];
const rta4 = [...elements, ...'random'];

const obj = [
	{ title: 'título', body: 'body' },
	{ title: 'título', body: 'body' },
];
const rta5 = [...elements, obj];
const rta6 = [...elements, ...obj];
console.log(rta3);
console.log(rta4);
console.log('..., obj', rta5);
console.log('..., ...', rta6);

// Modificar un array con spread operator

console.log('elements', elements);
elements.push(...othersElements);
console.log('elements', elements);
