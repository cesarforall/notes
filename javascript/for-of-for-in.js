// Diferencia entre for...of y for...in
// for...in itera sobre las propiedades de un objeto. Si el objeto es un array, las propiedades serán los índices. En cambio, si itera sobre lo que conocemos como objeto (en Python un diccionario), las propiedades son los keys.
// for...of itera sobre las elementos de una colección. Pasa por cada elemento

const productList = [];
productList.push({
    name: 'Bike',
    price: '120',
    image: 'https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
})
productList.push({
    name: 'Skateboard',
    price: '20',
    image: 'https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
})
productList.push({
    name: 'Bed',
    price: '40',
    image: 'https://images.pexels.com/photos/276517/pexels-photo-276517.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
})


for (product of productList) {
    console.log(product)
    for (key in product) {
        console.log(product[key])
    }
}