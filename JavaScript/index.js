// JavaScript para mostrar y ocultar el formulario
document.getElementById('btnAgregarDeportista').addEventListener('click', function() {
    var formulario = document.getElementById('formularioAgregar');
    formulario.style.display = (formulario.style.display === 'none' || formulario.style.display === '') ? 'block' : 'none';
});

// JavaScript para evitar que el formulario se envíe y la página se recargue
document.getElementById('formularioAgregar').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar que se envíe el formulario y recargue la página
    // Agrega aquí la lógica para guardar el deportista en la base de datos o hacer lo que sea necesario
});