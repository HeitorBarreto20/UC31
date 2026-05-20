from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Inicio')
def FunçãoInicio():
    return render_template ('página.principal.html')

@app.route('/Cardápio')
def FunçãoCardápio():
    return render_template ('cardapio.html')

@app.route('/Cliente')
def FunçãoCliente():
    return render_template ('cliente.html')

@app.route('/Contato')
def FunçãoContato():
    return render_template ('contato.html')

@app.route('/Lanche')
def FunçãoLanche():
    return render_template ('lanche.html')

@app.route('/Pedidos')
def FunçãoPedidos():
    return render_template ('pedidos.html')
    
if __name__ == '__main__':
    app.run(debug=True)