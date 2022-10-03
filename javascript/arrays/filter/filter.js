// El método filter devuele un nuevo array con los elementos que cumplan una condición

const words = ['spray', 'limit', 'elite', 'exuberant'];

const newArray = [];
for (let index = 0; index < words.length; index++) {
	const item = words[index];
	if (item.length >= 6) {
		newArray.push(item);
	}
}
console.log('newArray', newArray);
console.log('original', words);

const rta = words.filter(item => item.length >= 6);
console.log('rta', rta);
console.log('original', words);

const orders = [
	{
		customerName: 'Nicolas',
		total: 60,
		delivered: true,
	},
	{
		customerName: 'Zulema',
		total: 120,
		delivered: false,
	},
	{
		customerName: 'Santiago',
		total: 180,
		delivered: true,
	},
	{
		customerName: 'Valentina',
		total: 240,
		delivered: true,
	},
	{
		customerName: 'Nicolas',
		total: 2322,
		delivered: false,
	},
];

const rta3 = orders.filter(order => order.delivered);
console.log('rta3', rta3);

const rta4 = orders.filter(order => order.delivered && order.total >= 100);
console.log('rta4', rta4);

const search = query => {
	return orders.filter(order => {
		return order.customerName.includes(query);
	});
};
console.log(search('col'))