// Este ejemplo se usa realmente en lab-tools-app
// Crear una imagen con una promesa

function testImage(url) {
	// Define the promise
	const imgPromise = new Promise(function imgPromise(resolve, reject) {
		// Create the image
		const imgElement = new Image();

		// When image is loaded, resolve the promise
		imgElement.addEventListener('load', function imgOnLoad() {
			resolve(this);
		});

		// When there's an error during load, reject the promise
		imgElement.addEventListener('error', function imgOnError() {
			reject();
		});

		// Assign URL
		imgElement.src = url;
	});

	return imgPromise;
}

// Testear

testImage(`../../data/img-repuestos-pax/${partNumber}.jpg`).then(
	function fulfilled() {
		imgElement.setAttribute('src', `../../data/img-repuestos-pax/${partNumber}.jpg`);
	},

	function rejected() {
		imgElement.setAttribute('src', `../../data/img-repuestos-pax/anuncio.jpg`);
	},
);
