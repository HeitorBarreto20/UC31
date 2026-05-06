from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ola/<nome>')
def saudacao(nome):
    return f"Olá, {nome}! Seja bem-vindo!"

@app.route('/calculo/<int:n1>/<int:n2>')
def conta (n1, n2):
    resultado = n1 + n2
    return f"A soma de {n1} + {n2} = {resultado}!"

@app.route('/idade/<nome>/<int:idade>')
def nome_idade (nome, idade):
    if idade >= 18:
        return f"Seu nome é {nome} e sua idade é {idade} e é maior/igual de dezoito!"
    else:
        return f"Seu nome é {nome} e sua idade é {idade} e é menor de dezoito!"

@app.route('/produto/<nome>/<float:preco>')
def nome_preço (nome, preço):
    return f"Seu produto é {nome} e seu preço é {preço}!"

@app.route('/repetir/<palavra>/<int:vezes>')
def repetir (palavra, vezes):
    return (palavra + ' ') * vezes

if __name__ == '__main__':
    app.run(debug=True)