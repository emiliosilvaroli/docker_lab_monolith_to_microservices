from flask import Flask, request
import datetime
import uuid
import os

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
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return f"Risultato: {a + b}"
    except:
        print("Errore irreversibile: uscita immediata.")
        os._exit(1)

@app.route('/uuid')
def get_uuid():
    return str(uuid.uuid4())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
