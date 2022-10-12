// El método flatMap aplana un array y transforma los elementos mientras hace la iteración
// Sólo baja 1 nivel

const users = [
	{ userId: 1, username: 'Tom', attributes: ['Nice', 'Cute'] },
	{ userId: 2, username: 'Mike', attributes: ['Lovely'] },
	{ userId: 3, username: 'Nico', attributes: ['Nice', 'Cool'] },
];

const rta = users.map(user => user.attributes).flat();
console.log('map & flat', rta);

const rta2 = users.flatMap(user => user.attributes);
console.log('flatmap', rta2);

// Aplanar un array y obtener valores de objetos anidados

const calendars = {
	primaryCalendar: [
		{
			startDate: new Date(2021, 1, 1, 15),
			endDate: new Date(2021, 1, 1, 15, 30),
			title: 'Cita 1',
		},
		{
			startDate: new Date(2021, 1, 1, 17),
			endDate: new Date(2021, 1, 1, 18),
			title: 'Cita 2',
		},
	],
	secondaryCalendar: [
		{
			startDate: new Date(2021, 1, 1, 12),
			endDate: new Date(2021, 1, 1, 12, 30),
			title: 'Cita 2',
		},
		{
			startDate: new Date(2021, 1, 1, 9),
			endDate: new Date(2021, 1, 1, 10),
			title: 'Cita 4',
		},
	],
};

// Obtener el valor total de palabras

const rta3 = Object.values(calendars).flatMap(dates => dates.map(date => date.startDate));
console.log(rta3);

const text = [
	'Beautiful is better than ugly',
	'Explicit is better than implicit',
	'Simple is better than complex',
	'Complex is better than complicated',
];

// function solution(lines) {
// 	return lines.map(line => line.split(' ').length).reduce((sum, item) => (sum += item));
// }
function solution(lines) {
	return lines.flatMap(line => line.split(' ').length).reduce((sum, item) => (sum += item));
}

console.log(solution(text));
