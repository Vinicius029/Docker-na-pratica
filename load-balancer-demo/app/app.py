from flask import Flask, jsonify
import socket
import os
import time

app = Flask(__name__)

# Pegar informações do container
HOSTNAME = socket.gethostname()
CONTAINER_ID = os.getenv('HOSTNAME', 'unknown')

request_count = 0

@app.route('/')
def home():
    global request_count
    request_count += 1
    
    return jsonify({
        'message': 'Load Balancer Demo!',
        'servidor': HOSTNAME,
        'container_id': CONTAINER_ID[:12],
        'requisicoes_atendidas': request_count,
        'timestamp': time.time()
    })

@app.route('/slow')
def slow():
    """Simula uma requisição lenta"""
    time.sleep(2) 
    global request_count
    request_count += 1
    return jsonify({
        'message': 'Requisição lenta processada!',
        'servidor': HOSTNAME,
        'tempo': '2 segundos'
    })

@app.route('/stats')
def stats():
    """Estatísticas do servidor"""
    return jsonify({
        'servidor': HOSTNAME,
        'total_requisicoes': request_count,
        'uptime': time.time()
    })

if __name__ == '__main__':
    print(f"🐳 Servidor iniciado: {HOSTNAME}")
    app.run(host='0.0.0.0', port=5000, debug=True)