// El reto es conseguir filtrar desde 3 inputs distintos que van erando los mismo filtros

manufacturerListElement.addEventListener('change', e => {
	const optionValue = manufacturerListElement.options[manufacturerListElement.selectedIndex].text;
	console.log(optionValue);
	if (optionValue === 'FABRICANTE') {
		currentSpareParts = [...repuestosData];
		createOptions([], modelListElement, 'MODELO');
		createOptions([], versionModelListElement, 'VERSIÓN');
		displaySpareParts(currentSpareParts);
	}
	if (optionValue != 'FABRICANTE') {
		findSparePartsByCategory('FABRICANTE', optionValue);
		const modelList = getModelList(optionValue);
		createOptions(modelList, modelListElement, 'MODELO');
	}
});

modelListElement.addEventListener('change', e => {
	const optionValue = modelListElement.options[modelListElement.selectedIndex].text;
	const fatherValue = manufacturerListElement.options[manufacturerListElement.selectedIndex].text;
	console.log(fatherValue);
	if (optionValue === 'MODELO') {
		currentSpareParts = [...repuestosData];
		createOptions([], versionModelListElement, 'VERSIÓN');
		findSparePartsByCategory('FABRICANTE', fatherValue);
	}
	if (optionValue != 'MODELO') {
		currentSpareParts = [...repuestosData];
		findSparePartsByCategory('FABRICANTE', fatherValue);
		findSparePartsByCategory('MODELO', optionValue);
		const versionList = getVersionList(optionValue);
		createOptions(versionList, versionModelListElement, 'VERSIÓN');
	}
});

versionModelListElement.addEventListener('change', e => {
	const optionValue = versionModelListElement.options[versionModelListElement.selectedIndex].text;
	const fatherValue = modelListElement.options[modelListElement.selectedIndex].text;
	const grandFatherValue = manufacturerListElement.options[manufacturerListElement.selectedIndex].text;
	if (optionValue === 'VERSIÓN') {
		currentSpareParts = [...repuestosData];
		findSparePartsByCategory('FABRICANTE', grandFatherValue);
		findSparePartsByCategory('MODELO', fatherValue);
	}
	if (optionValue != 'VERSIÓN') {
		currentSpareParts = [...repuestosData];
		findSparePartsByCategory('FABRICANTE', grandFatherValue);
		findSparePartsByCategory('MODELO', fatherValue);
		findSparePartsByCategory('VERSIÓN', optionValue);
	}
});