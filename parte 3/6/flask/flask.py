from flask import Flask
app = Flask(__name__)

@app.route("/")
# ruta donde se va a ejecutar la funcioon, osea en el navegador
#"/" se va a ejecutar en lapagina principal

def hola_mundo():
    return "Hola mundo!!"
if __name__ == "__main__":
    app.run()