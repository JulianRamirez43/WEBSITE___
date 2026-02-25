from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite conexión con frontend (ej: Vercel)

# Ruta principal
@app.route("/")
def home():
    return jsonify({
        "message": "Backend funcionando correctamente 🚀"
    })

# Ruta para productos (ejemplo ecommerce)
@app.route("/productos", methods=["GET"])
def obtener_productos():
    productos = [
        {
            "id": 1,
            "nombre": "Manilla Oro 18K",
            "precio": 250000,
            "imagen": "https://tusitio.com/img1.jpg"
        },
        {
            "id": 2,
            "nombre": "Manilla Oro Laminado",
            "precio": 90000,
            "imagen": "https://tusitio.com/img2.jpg"
        }
    ]
    return jsonify(productos)

# Ruta para contacto
@app.route("/contacto", methods=["POST"])
def contacto():
    data = request.json
    nombre = data.get("nombre")
    mensaje = data.get("mensaje")

    return jsonify({
        "status": "Mensaje recibido",
        "nombre": nombre,
        "mensaje": mensaje
    })

if __name__ == "__main__":
    app.run(debug=True)
    #test