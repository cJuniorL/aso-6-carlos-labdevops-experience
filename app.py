from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
<<<<<<< HEAD
    return "Carlos Roberto"
=======
    return "Hello World"
>>>>>>> 3bdd9d95594ce55b37ace38bf6b9c4885cb33ecf

if __name__ == '__main__':
    app.run()