from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'chave_secreta'

@app.route('/contador', methods=['GET', 'POST'])
def contador():
    if request.method == 'POST':
        session.pop('contador', None)
        return redirect(url_for('contador'))

    session['contador'] = session.get('contador', 0) + 1

    return render_template('contador.html', acessos=session['contador'])

if __name__ == '__main__':
    app.run(debug=True)