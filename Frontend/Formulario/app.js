const loginForm = document.getElementById('login-form');
const message = document.getElementById('message');

loginForm.addEventListener('submit', function (e) {
	e.preventDefault(); // prevenir el comportamiento por defecto del formulario

	const username = loginForm.username.value;
	const password = loginForm.password.value;

	if (password === 'contraseña') {
		// Si la contraseña es correcta
		loginForm.style.display = 'none'; // ocultar el formulario de inicio de sesión
		message.innerText = 'Inicio de sesión correcto.'; // agregar un mensaje de éxito
	} else {
		message.innerText = 'Contraseña incorrecta. Inténtalo de nuevo.'; // agregar un mensaje de error
	}
});
