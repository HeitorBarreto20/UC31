from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/index", methods=["GET", "POST"])
def index():
    mensagem = ""

    if request.method == "POST":
        
        nickname = request.form["nickname"]
        jogo = request.form["jogo"]
        email = request.form["email"]

        if not nickname or len(nickname) < 4 or not jogo or not email:
            mensagem = "Preencha todos os campos obrigatórios."
        else:
            mensagem = "Inscrição realizada com sucesso!"

    return render_template("index.html", mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)