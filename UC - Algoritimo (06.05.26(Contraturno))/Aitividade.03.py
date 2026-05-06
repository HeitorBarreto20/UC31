from flask import Flask

app = Flask(__name__)

@app.route('/arearestrita/<int:id>')
def area_restrita(id):
    if id == 1:
        return 'Cadeado fechado'
    elif id == 2:
        return 'Cadeado aberto'
    else:
        return 'ID inválido'

if __name__ == '__main__':
    app.run()