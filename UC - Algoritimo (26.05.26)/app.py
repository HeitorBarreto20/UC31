from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.atividade.html")

@app.route("/cursos")
def cursos():
    return render_template("cursos.atividade.html")

@app.route("/professores")
def professores():
    return render_template("professores.atividade.html")

@app.route("/contato")
def contato():
    return render_template("contato.atividade.html")

if __name__ == "__main__":
    app.run(debug=True)