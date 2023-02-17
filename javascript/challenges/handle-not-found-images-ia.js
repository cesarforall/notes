async function createImageComponentAsync({ src, defaultSrc, alt, imgAttributes = {}, containerAttributes = {} }) {
	const container = document.createElement('div');
	container.classList.add('image-container');
	Object.keys(containerAttributes).forEach(key => {
		container.setAttribute(key, containerAttributes[key]);
	});

	const image = document.createElement('img');
	image.alt = alt;
	Object.keys(imgAttributes).forEach(key => {
		image.setAttribute(key, imgAttributes[key]);
	});

	try {
		await loadImageAsync(image, src);
	} catch (error) {
		console.error(`Error loading image: ${src}`, error);
		image.src = defaultSrc;
	}

	container.appendChild(image);

	return container;
}
