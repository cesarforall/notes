const products = [
	{ title: 'Pizza', price: 121, id: '🍕' },
	{ title: 'Burger', price: 121, id: '🍔' },
	{ title: 'Hot cakes', price: 121, id: '🥞' },
];
const myProducts = [];
console.log('products', products);
console.log('myProducts', myProducts);
console.log('-'.repeat(10));

// push

// const product = products.find(item => item.id === '🍔');
// if (product) {
// 	myProducts.push(product);
// }
// console.log('products', products);
// console.log('myProducts', myProducts);
// console.log('-'.repeat(10));

const productIndex = products.findIndex(item => item.id === '🍔');
if (productIndex != -1) {
	myProducts.push(products[productIndex]);
	// El método splice modifica un array desde un índice
	// El primer parámetro es el índice de inicio, el segundo el número de posiciones y el tercero un valor para sobreescribir
	// Si no se especifica el tercer parámetro se elimina lo que hay dentro de la posición
	products.splice(productIndex, 1);
}
console.log('products', products);
console.log('myProducts', myProducts);
console.log('-'.repeat(10));

// Challenge - Generar un nuevo array sin un elemento
const arrayChallenge = products.filter(item => item.id != '🍔');
console.log(arrayChallenge);

// Update
const productsV2 = [
	{ title: 'Pizza', price: 121, id: '🍕' },
	{ title: 'Burger', price: 121, id: '🍔' },
	{ title: 'Hot cakes', price: 121, id: '🥞' },
];

const update = {
	id: '🥞',
	changes: {
		price: 200,
		description: 'delicious',
	},
};

let productsV2Id = productsV2.findIndex(item => item.id === update.id);
if (productsV2Id != -1) {
	// Para actualizar un objeto se crea un objeto con los mismos entries con spread operator
	// Luego se añaden los nuevos entries, que sería otro iterable, con spread operator
	productsV2[productsV2Id] = { ...productsV2[productsV2Id], ...update.changes };
}
console.log(productsV2);

// Challenge - Hacer una modificación sin modificar el array original
const productsV3 = [
	{ title: 'Pizza', price: 121, id: '🍕' },
	{ title: 'Burger', price: 121, id: '🍔' },
	{ title: 'Hot cakes', price: 121, id: '🥞' },
];

let arrayChallengeV3 = [];

if (productsV2Id) {
	arrayChallengeV3 = productsV3.map(item => {
		if (item.id === update.id) {
			return {
				...item,
				...update.changes,
			};
		}
		return { ...item };
	});
}
console.log('productsV3', productsV3);
console.log('arrayChallengeV3', arrayChallengeV3);