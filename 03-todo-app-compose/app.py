from flask import Flask, render_template_string, request, redirect
import psycopg2
import os
import time

app = Flask(__name__)

# Configuração do banco
DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('DB_NAME', 'todoapp')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASS', 'senha123')

def get_db_connection():
    max_retries = 5
    for i in range(max_retries):
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            return conn
        except psycopg2.OperationalError:
            if i < max_retries - 1:
                print(f"Tentativa {i+1} falhou. Tentando novamente em 2 segundos...")
                time.sleep(2)
            else:
                raise

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id SERIAL PRIMARY KEY,
            descricao TEXT NOT NULL,
            concluida BOOLEAN DEFAULT FALSE
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, descricao, concluida FROM tarefas ORDER BY id')
    tarefas = cur.fetchall()
    cur.close()
    conn.close()
    
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>TODO App - Docker Compose</title>
        <style>
            body { font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px; }
            h1 { color: #2c3e50; }
            .tarefa { padding: 10px; margin: 10px 0; background: #ecf0f1; border-radius: 5px; }
            .concluida { text-decoration: line-through; opacity: 0.6; }
            input[type="text"] { width: 70%; padding: 10px; }
            button { padding: 10px 20px; background: #3498db; color: white; border: none; cursor: pointer; }
            button:hover { background: #2980b9; }
            .delete { background: #e74c3c; }
            .delete:hover { background: #c0392b; }
        </style>
    </head>
    <body>
        <h1>TODO App com Docker Compose</h1>
        <p>Aplicação rodando em containers separados!</p>
        
        <form method="POST" action="/adicionar">
            <input type="text" name="descricao" placeholder="Nova tarefa..." required>
            <button type="submit">Adicionar</button>
        </form>
        
        <h2>Tarefas:</h2>
        {% for tarefa in tarefas %}
        <div class="tarefa {% if tarefa[2] %}concluida{% endif %}">
            <strong>{{ tarefa[1] }}</strong>
            <form method="POST" action="/concluir/{{ tarefa[0] }}" style="display: inline;">
                <button type="submit">✓ Concluir</button>
            </form>
            <form method="POST" action="/deletar/{{ tarefa[0] }}" style="display: inline;">
                <button type="submit" class="delete">Deletar</button>
            </form>
        </div>
        {% endfor %}
    </body>
    </html>
    '''
    return render_template_string(html, tarefas=tarefas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    descricao = request.form['descricao']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO tarefas (descricao) VALUES (%s)', (descricao,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

@app.route('/concluir/<int:id>', methods=['POST'])
def concluir(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE tarefas SET concluida = TRUE WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

@app.route('/deletar/<int:id>', methods=['POST'])
def deletar(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM tarefas WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    print("Iniciando aplicação...")
    print(f"Conectando em {DB_HOST}:{DB_NAME}")
    init_db()
    print("Banco de dados inicializado!")
    app.run(host='0.0.0.0', port=8080, debug=True)