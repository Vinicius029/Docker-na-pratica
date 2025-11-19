from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return f'''
    Todo List com Postgres e Docker
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)