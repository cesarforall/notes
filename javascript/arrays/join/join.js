const elements = ['fire', 'Air', 'Water'];

let rtaFinal = '';
const separator = '--';

for (let index = 0; index < elements.length; index++) {
	const element = elements[index];
	rtaFinal = rtaFinal + element + separator;
}
console.log('for', rtaFinal);

// El método join unifica los elementos de un array

const rta = elements.join('--');
console.log('rta', rta);

const title = 'Curso de manipulación de arrays';
const titleFinal = title.split(' ').join('-').toLowerCase();
console.log(titleFinal);
