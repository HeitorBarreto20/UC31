from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("Inicio.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/servicos")
def servicos():
    return render_template("servicos.html")

if __name__ == '__main__':
    app.run(debug=True)