from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('Questão.01.html')

@app.route('/alunos')
def alunos():
    alunos = [
        {"nome": "Alice", "matricula": "123"},
        {"nome": "Bruno", "matricula": "456"},
        {"nome": "Clara", "matricula": "789"}
    ]
    return render_template('Questão.02.html', alunos=alunos)

app.run()