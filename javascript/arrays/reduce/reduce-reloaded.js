// const items = [1, 3, 2, 3];
const items = [1, 3, 2, 3, 3, 1, 10];

const rta = items.reduce((obj, item) => {
	if (!obj[item]) {
		obj[item] = 1;
	} else {
		obj[item] += 1;
	}
	return obj;
}, {});
console.log(rta);

const data = [
	{
		name: 'Nicolas',
		level: 'low',
	},
	{
		name: 'Andrea',
		level: 'medium',
	},
	{
		name: 'Zulema',
		level: 'hight',
	},
	{
		name: 'Santiago',
		level: 'low',
	},
	{
		name: 'Valentina',
		level: 'medium',
	},
	{
		name: 'Lucia',
		level: 'hight',
	},
];

const rta2 = data
	.map(item => item.level)
	.reduce((obj, item) => {
		if (!obj[item]) {
			obj[item] = 1;
		} else {
			obj[item] += 1;
		}
		return obj;
	}, {});
console.log(rta2);

// Challenge - Acumular en rangos

function toRank(array) {
	const ranking = array.reduce(
		(obj, item) => {
			if (item > 0 && item < 6) {
				obj['1-5'] += 1;
			} else if (item > 5 && item < 9) {
				obj['6-8'] += 1;
			} else if (item > 8 && item < 11) {
				obj['9-10'] += 1;
			}
			return obj;
		},
		{
			'1-5': 0,
			'6-8': 0,
			'9-10': 0,
		},
	);
	return ranking;
}
const ranking = toRank([1, 2, 3, 7, 9]);
console.log(ranking);
