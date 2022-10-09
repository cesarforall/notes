// El método includes retorna True o False
// Se le pasa como argumento el elemento que estamos buscando
// Funciona con arrays y strings

const pets = ['cat', 'dog', 'bat'];

let includeInArray = false;

for (let index = 0; index < pets.length; index++) {
	const element = pets[index];
	if (element === 'dog') {
		includeInArray = true;
		break;
	}
}
console.log('for', includeInArray);

const rta2 = pets.includes('dog');
console.log('includes', rta2);