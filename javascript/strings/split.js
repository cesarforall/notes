// El método split separa los caracteres de un string en un array
// Se envía como argumento el caracter separador, por ejemplo, un espacio

const title = 'Curso de manipulación de strings';
const titleFinal = title.split(' ').join('-').toLowerCase();
console.log(titleFinal);