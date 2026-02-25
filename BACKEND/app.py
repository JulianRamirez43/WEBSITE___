from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Esto permite que el JS del frontend pueda entrar aquí

@app.route('/contacto', methods=['POST'])
def contacto():
    datos = request.json
    email_recibido = datos.get('correo')
    
    print(f"Log en consola: Alguien se registró con {email_recibido}")
    
    # Aquí es donde podrías guardar en una base de datos más adelante
    return jsonify({"status": "ok", "mensaje": "¡Éxito! Datos recibidos en Python"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    