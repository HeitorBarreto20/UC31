from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('index.02.html')

@app.route('/resultado')
def resultado():
    nome = request.args.get('nome')
    curso = request.args.get('curso')
    cidade = request.args.get('cidade')

    return render_template(
        'resultado.html',
        nome=nome,
        curso=curso,
        cidade=cidade
    )

if __name__ == '__main__':
    app.run(debug=True)