from flask import Flask, request
import datetime
import uuid

app = Flask(__name__)

@app.route('/')
def home():
    return "Benvenuto nel monolite!"

@app.route('/echo')
def echo():
    msg = request.args.get('msg', '')
    return f"Hai detto: {msg}"

@app.route('/time')
def time():
    return f"Ora corrente: {datetime.datetime.now()}"

@app.route('/math/add')
def add():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return f"Risultato: {a + b}"
    except:
        return "Errore: parametri non validi", 400

@app.route('/uuid')
def get_uuid():
    return str(uuid.uuid4())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
