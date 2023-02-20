function displaySpareParts(data) {
	sparePartsContainer.innerText = '';
	const partsLength = data.length;
	partsLengthElement.innerText = `${partsLength} repuestos compatibles`;

	// create observer instance
	const observer = new IntersectionObserver((entries, observer) => {
		entries.forEach(entry => {
			if (entry.isIntersecting) {
				const card = entry.target;
				const img = card.querySelector('img');
				img.setAttribute('src', img.getAttribute('data-src'));
				img.onload = () => {
					card.classList.add('loaded');
				};
				observer.unobserve(card);
			}
		});
	});

	// create and append cards
	const cards = data.map(item => {
		const partNumber = item['Part number'] || '';
		const partName = item['Parts name'] || '';
		const repairComponent = item['Repair component'] || '';
		const remark = item['Remark'] || '';
		const compatibleDevices = item['Compatible device'];
		const card = createSparePartCard(partNumber, partName, repairComponent, remark, compatibleDevices);

		// observe the card
		observer.observe(card);

		return card;
	});

	// append cards to container
	sparePartsContainer.append(...cards);
}

function createSparePartCard(partNumber, partName, repairComponent, remark, compatibleDevicesArray) {
	const compatibleDevices = [];
	if (compatibleDevicesArray) {
		compatibleDevicesArray.forEach(item => {
			const id = item[0];
			const device = versionesData.find(item => item.id == id);

			const versionName = `<span>${device.name}</span><br>`;
			compatibleDevices.push(versionName);
		});
	}
	let compatibleDevicesHTML = ``;
	compatibleDevices.forEach(item => (compatibleDevicesHTML += item));

	const articleElement = document.createElement('article');
	articleElement.classList.add('card');

	const imgContainerElement = document.createElement('article');
	imgContainerElement.classList.add('card-img-container');

	const imgElement = document.createElement('img');
	imgElement.classList.add('card-img');
	imgElement.setAttribute('data-src', `../../data/img-repuestos-pax/${partNumber}.jpg`);
	imgElement.setAttribute('alt', 'spare part');

	const io = new IntersectionObserver((entries, observer) => {
		entries.forEach(entry => {
			if (entry.isIntersecting) {
				const img = entry.target;
				img.setAttribute('src', img.getAttribute('data-src'));
				img.onload = () => {
					imgContainerElement.classList.add('loaded');
				};
				img.onerror = () => {
					img.setAttribute('src', `../../data/img-repuestos-pax/anuncio.jpg`);
					imgContainerElement.classList.add('loaded');
				};
				observer.unobserve(img);
			}
		});
	});

	io.observe(imgElement);

	const tableElement = document.createElement('table');
	tableElement.classList.add('card-table');
	tableElement.innerHTML = `
	  <tbody>
	  <tr>
		  <td class="left">Part number</td>
		  <td class="right">${partNumber}</td>
	  </tr>
	  <tr>
		  <td class="left">Part name</td>
		  <td class="right">${partName}</td>
	  </tr>
	  <tr>
		  <td class="left">Repair component</td>
		  <td class="right">${repairComponent}</td>
	  </tr>
	  <tr>
		  <td class="left">Remark</td>
		  <td class="right">${remark}</td>
	  </tr>
	  <tr>
		  <td class="left">Compatible devices</td>
		  <td class="right">${compatibleDevicesHTML}</td>
	  </tr>
	  </tbody>
	  `;

	imgContainerElement.append(imgElement);
	articleElement.append(imgContainerElement);
	articleElement.append(tableElement);
	return articleElement;
}
