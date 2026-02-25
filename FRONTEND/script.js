const formulario = document.getElementById('miFormulario');
const textoMensaje = document.getElementById('mensaje');

formulario.addEventListener('submit', async (e) => {
    e.preventDefault(); // Evita que la página se recargue
    const email = document.getElementById('email').value;

    try {
        // Hacemos la llamada al backend de Python
        const respuesta = await fetch('http://127.0.0.1:5000/contacto', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ correo: email })
        });

        const datos = await respuesta.json();
        textoMensaje.innerText = datos.mensaje; // Muestra "¡Éxito!" en la pantalla
    } catch (error) {
        textoMensaje.innerText = "Error al conectar con el servidor.";
    }
});