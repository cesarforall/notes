const loginForm = document.getElementById('login-form');
const fileInput = document.getElementById('file-input');
const successMessage = document.getElementById('success-message');

loginForm.addEventListener('submit', function (e) {
	e.preventDefault(); // prevenir el comportamiento por defecto del formulario

	const username = loginForm.username.value;
	const password = loginForm.password.value;

	if (password === 'contraseña') {
		// Si la contraseña es correcta
		loginForm.style.display = 'none'; // ocultar el formulario de inicio de sesión
		successMessage.style.display = 'block'; // mostrar el mensaje de éxito
		fileInput.style.display = 'block'; // mostrar el campo de entrada de archivo
	} else {
		successMessage.innerText = 'Contraseña incorrecta. Inténtalo de nuevo.'; // agregar un mensaje de error
	}
});
