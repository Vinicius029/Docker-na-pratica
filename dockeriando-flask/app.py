from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1> Meu servidor Docker!<h1/>
    <p> Esta aplicação está rondando dentro de um container</p>
    '''

@app.route('/sobre')
def sobre():
    return '''
    <h2>Está uma pagina sobre o Docker<h2/>
    '''

@app.route('/ola/<nome>')
def ola(nome):
    return f'<h1>Olá, {nome}! Bem-vindo ao Docker! 🐳</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
