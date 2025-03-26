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
    # Nessun try-except: input errati causano crash
    a = float(request.args.get('a'))  # se manca o è errato => ValueError
    b = float(request.args.get('b'))
    return f"Risultato: {a + b}"

@app.route('/uuid')
def get_uuid():
    return str(uuid.uuid4())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
