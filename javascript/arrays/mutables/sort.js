// El método sort ordena los elementos

// Ordena los caracteres según el orden ASCII
const months = ['March', 'Jan', 'Feb', 'Dec'];
months.sort();
console.log(months);

// Ordena los números según el código ASCII
// const numbers = [1, 30, 4, 21, 100000];
// numbers.sort();
// console.log(numbers);

const numbers = [1, 30, 4, 21, 100000];
// Para ordenar según el orden de números
// numbers.sort((a, b) => a - b);
// Para ordenar los números de forma inversa
numbers.sort((a, b) => b - a);
console.log(numbers);

const words = ['réservé', 'premier', 'communiqué', 'café', 'adieu', 'éclair', 'banana'];
// words.sort();
// Para comparar en versiones antiguas

words.sort((a, b) => a.localeCompare(b));
console.log(words);

// sort con objetos
const orders = [
	{
		customerName: 'Nicolas',
		total: 600,
		delivered: true,
	},
	{
		customerName: 'Zulema',
		total: 120,
		delivered: false,
	},
	{
		customerName: 'Santiago',
		total: 1840,
		delivered: true,
	},
	{
		customerName: 'Valentina',
		total: 240,
		delivered: true,
	},
];

orders.sort((a, b) => b.total - a.total);
console.log(orders);

// Challenge - Reto con fechas en un array de objetos

const ordersV2 = [
	{
		customerName: 'Nicolas',
		total: 600,
		delivered: true,
        // Las fechas en este formato se tratan de forma local. En esta fecha cuenta el uso horario y horario de verano
		date: new Date(2020, 3, 15, 15, 30),
	},
	{
		customerName: 'Zulema',
		total: 120,
		delivered: false,
        // Las fechas en este formato se tratan de forma local. Por lo tanto, el uso horario en España es +1
		date: new Date(2019, 1, 1, 16),
	},
	{
		customerName: 'Santiago',
		total: 1840,
		delivered: true,
		date: new Date(2021, 1, 1, 10),
	},
	{
		customerName: 'Valentina',
		total: 240,
		delivered: true,
		date: new Date(2018, 1, 1, 20),
	},
];
ordersV2.sort((a, b) => a.date - b.date);
console.log(ordersV2);

const array = [['🐸','🐱'],'🐹', ['🐯']]; 
const rta = array.flat();
console.log("🚀 ~ file: sort.js ~ line 89 ~ rta", rta)
