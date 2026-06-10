from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/')
def inicio():
    nome = request.cookies.get('nome')
    email = request.cookies.get('email')
    tema = request.cookies.get('tema', 'claro')

    return render_template(
        'inicio.html',
        nome=nome,
        email=email,
        tema=tema
    )


@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form.get('nome')
    email = request.form.get('email')

    resposta = make_response(redirect('/'))

    resposta.set_cookie('nome', nome, max_age=60 * 60 * 24 * 30)
    resposta.set_cookie('email', email, max_age=60 * 60 * 24 * 30)

    return resposta


@app.route('/tema/<modo>')
def alterar_tema(modo):
    resposta = make_response(redirect('/'))

    if modo in ['claro', 'escuro']:
        resposta.set_cookie('tema', modo, max_age=60 * 60 * 24 * 30)

    return resposta


if __name__ == '__main__':
    app.run(debug=True)