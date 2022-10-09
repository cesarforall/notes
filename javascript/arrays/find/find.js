// El método find devuelve el primer elemento que cumpla una condición
// Si no encuentra un elemento retorna undefined

const numbers = [1, 30, 39, 29, 10, 13];

for (let index = 0; index < numbers.length; index++) {
	const element = numbers[index];
	if (element === 30) {
		rta = element;
		break;
	}
}
console.log('rta', rta);

const rta2 = numbers.find(item => item === 30);
console.log('rta2', rta2);

const products = [
	{
		name: 'Pizza',
		price: 12,
		id: '🍕',
	},
	{
		name: 'Burger',
		price: 23,
		id: '🍔',
	},
	{
		name: 'Hot dog',
		price: 34,
		id: '🌭',
	},
	{
		name: 'Hot cakes',
		price: 355,
		id: '🥞',
	},
];

const rta3 = products.find(item => item.id === '🍔');
console.log('rta3', rta3);

// El método findIndex devuelve la posición donde se encuentra el primer elemento que cumpla una condición
// Si no encuentra un elemento retorna -1

const rta4 = products.findIndex(item => item.id === '🍔');
console.log('rta4', rta4);