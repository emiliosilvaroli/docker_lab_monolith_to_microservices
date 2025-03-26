from flask import Flask, request
import os
app = Flask(__name__)

@app.route('/math/add')
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return f"Risultato: {a + b}"
    except:
        print("Errore irreversibile: uscita immediata.")
        os._exit(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
