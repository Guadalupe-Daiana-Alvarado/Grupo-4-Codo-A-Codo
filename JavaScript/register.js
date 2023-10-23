document.addEventListener('DOMContentLoaded', function() {
    // Tu código JavaScript aquí
    const nombre = document.getElementById('nombreUsuario');
    const correo = document.getElementById('correoElectronico');
    const pass = document.getElementById('contraseña');
    const form = document.querySelector('form');
    const parrafo = document.getElementById('warnings');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        let warning = '';
        let entrar = false;
        let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        
        if (nombre.value.length < 6) {
            warning += `El nombre no es válido <br>`;
            entrar = true;
        }
        
        if (!regexEmail.test(correo.value)) {
            warning += `El correo no es válido <br>`;
            entrar = true;
        }
        
        if (pass.value.length < 8) {
            warning += `La contraseña no es válida <br>`;
            entrar = true;
        }
        
        if (entrar) {
            parrafo.innerHTML = warning;
        }
    });
});
