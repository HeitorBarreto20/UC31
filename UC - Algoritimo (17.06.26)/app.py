from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "chave_secreta"

USUARIO = "HB20"
SENHA = "senha.muito.criativa.gostou.professora?"

@app.route("/", methods=["GET", "POST"])
def inicio():
    erro = ""

    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == USUARIO and senha == SENHA:
            session["usuario"] = usuario
            return redirect("/restrita")
        else:
            erro = "Usuário ou senha inválidos!"

    return render_template("inicio.html", erro=erro)


@app.route("/restrita")
def restrita():
    if "usuario" not in session:
        return redirect("/")

    return render_template(
        "restrita.html",
        usuario=session["usuario"]
    )


@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)