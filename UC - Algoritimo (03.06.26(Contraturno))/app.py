from flask import Flask, render_template, request

app = Flask (__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/recebedados', methods=['POST'])
def receberdados():

    nome = request.form.get('nome', "").title()

    email = request.form.get('email', "").lower()

    telefone = request.form.get('telefone', "").strip()
    telefone = telefone.replace('(', '')
    telefone = telefone.replace(')', '')
    telefone = telefone.replace('-', '')

    cpf = request.form.get('cpf', "").strip()
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')

    cidade = request.form.get('cidade', "").strip()

    estado = request.form.get('estado', "").strip()

    curso = request.form.get('curso', "").strip()

    idade = request.form.get('idade', "").strip()

    senha = request.form.get('senha', "").strip()

    if len(nome) < 8:
        return f"Nome muito curto!"
    
    if "@" not in email or ".com" not in email:
        return f"Seu email deve conter '@' e '.com'!"
    
    if not len(telefone) == 11:
        return f"Telefone muito pequeno!"
    
    if len(cpf) > 11 or len(cpf) < 11:
        return f"CPF muito pequeno!"
    
    if len(cidade) < 3:
        return f"Cidade inválida!"
    
    if len(estado) > 2 or len(estado) < 2:
        return f"Estado inválido!"
    
    if curso == "":
        return f"Precisa ser preenchido!"
    
    if not int(idade):
        return f"A idade precisa ser em números!"
    
    if not int(idade) >= 16:
        return f"Você é muito novo!"
    
    if len(senha) < 8:
        return f"Senha curta!"
    
    return f"""
    Nome: {nome}<br>
    Email: {email}<br>
    Telefone: {telefone}<br>
    CPF: {cpf}<br>
    Cidade: {cidade}<br>
    Estado: {estado}<br>
    Curso: {curso}<br>
    Idade: {idade}<br>
    Senha: {senha}<br>
    Cadastro feito com sucesso!
    """

if __name__ == '__main__':
    app.run(debug=True)