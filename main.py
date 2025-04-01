from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/perfil/<usuario>.html')
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)

@freezer.register_generator
def perfil():
    yield 'perfil', {'usuario': 'user1'}
    yield 'perfil', {'usuario': 'user2'}
    # Adicione mais usuários conforme necessário

if __name__ == "__main__":
    freezer.freeze()