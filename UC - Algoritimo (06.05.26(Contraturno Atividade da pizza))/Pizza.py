from flask import Flask, render_template

app = Flask(__name__)

sabores_de_pizza = ["calabresa", "marguerita", "frango"]

@app.route('/pizzaria/<sabor>')
def pizzaria(sabor):
    if sabor == "calabresa":
        return render_template('calabresa.html', title='Pizza de Calabresa!')
    elif sabor == "marguerita":
        return render_template('marguerita.html', title='Pizza de Marguerita!')
    elif sabor == "frango":
        return render_template('frango.html', title='Pizza de Frango!')
    else:
        return f"Não temos esté sabor!"

if __name__ == '__main__':
    app.run(debug=True)