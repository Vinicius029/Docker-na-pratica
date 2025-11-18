from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/date')
def date():
    date = datetime.now()

    return f'''
    A hora do sistema é {date}
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)