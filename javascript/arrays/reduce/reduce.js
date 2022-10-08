// El método reduce de los arrays reduce todo a un solo valor

const totals = [1, 2, 3, 4];

let sum = 0;
for (let index = 0; index < totals.length; index++) {
	const element = totals[index];
	sum += element;
}
console.log(sum);

// arr.reduce(callback(acumulador, valorActual[, índice[, array]])[, valorInicial])
// arr.reduce((previousValue, currentValue) => previousValue + currentValue, initialValue);
// Los parámetros que recibe el método reduce son la función de callback y el valor o estado inicial del acumulador

const rta = totals.reduce((sum, element) => {
	sum + element;
}, 0);
console.log('rta: ', rta);
