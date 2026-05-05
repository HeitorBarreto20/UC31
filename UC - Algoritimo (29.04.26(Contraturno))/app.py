from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/contato')
def contato():
    nome = "Heitor"
    return render_template('index_html', title='Página Inicial', nome=nome)

@app.route('/usuario')
def usuario ():
    usuario = {'nome:' 'Heitor', 'email:' 'heit.barreto.09@gmail.com'}
    return render_template ('index.html', title='Página Inicial', usuario=usuario)

if __name__ == '__main__':
    app.run()