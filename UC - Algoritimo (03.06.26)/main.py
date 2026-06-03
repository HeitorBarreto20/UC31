from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('index.html')

@app.route('/validacao', methods=['POST'])
def casdastro():

    nome = request.form.get('nome', '').strip().tittle()
    email = request.form.get('email', '').strip().tittle()
    cidade = request.form.get('cidade', '').strip().tittle()

    return f"""
    Nome: {nome}<br>
    Email: {email}<br>
    Cidade: {cidade}
    """

if __name__ == '__main__':
    app.run()