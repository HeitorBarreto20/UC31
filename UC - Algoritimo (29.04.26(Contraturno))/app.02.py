from flask import Flask, render_template

app = Flask(__name__)

@app.route("/login")
def login():
    nome = "SeuNomeAqui"  # você pode trocar depois dinamicamente
    return render_template("login.html", nome=nome)

if __name__ == "__main__":
    app.run(debug=True)