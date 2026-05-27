from flask import Flask, render_template, request

app = Flask (__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/recebedados', methods=['POST'])
def receberdados():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    estado = request.form['estado']
    formacao = request.form['formacao']
    modalidade = request.form.getlist('modalidade')

    if senha == 12345:
        return "Senha correta! e {} e {} e {} e {} e {} e {}".format(nome, email, senha, estado, formacao, modalidade)
    else:
        return f"Senha errada!"

if __name__ == '__main__':
    app.run(debug=True)