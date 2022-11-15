from flask import Flask, render_template

app = Flask(__name__)

lista_usuarios = ['Brian', 'Costa', 'Teste']

app.config['SECRET_KEY'] = 'dcc92759b404cc3d1adf6e83265a0d1e'


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
