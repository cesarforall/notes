// El método findIndex devuelve la posición donde se encuentra el primer elemento que cumpla una condición
// Si no encuentra un elemento retorna -1

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

const rta = products.findIndex(item => item.id === '🍔');
console.log('rta', rta);
