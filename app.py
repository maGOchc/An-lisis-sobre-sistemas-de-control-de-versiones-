# Importamos Flask para crear la aplicación web.
# render_template permite mostrar archivos HTML de la carpeta templates.
from flask import Flask, render_template

# Creamos la aplicación Flask.
app = Flask(__name__)


# Definimos qué debe ocurrir cuando alguien visita la página principal "/".
@app.route("/")
def inicio():
    # Buscamos templates/index.html y lo enviamos al navegador.
    return render_template("index.html")


# Este bloque se ejecuta cuando iniciamos el archivo directamente.
if __name__ == "__main__":
    # Ejecutamos el servidor para hacer pruebas en nuestra computadora.
    # debug=True facilita encontrar errores durante el desarrollo local.
    # No debemos usar el modo debug en producción.
    app.run(debug=True)