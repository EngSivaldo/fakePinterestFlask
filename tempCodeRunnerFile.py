from flask import Flask, render_template


app = Flask(__name__)

#colocar no ar 

@app.route('/')
def homepage():
  return render_template("homepage.html")


@app.route('/perfil/<usuario>')
def perfil(usuario):
  return render_template("perfil.html", usuario=usuario)


#colocar no ar
if __name__ == "__main__":
  app.run(debug=True)
  
  