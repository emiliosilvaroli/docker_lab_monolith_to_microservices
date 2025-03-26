from flask import Flask, request
app = Flask(__name__)

@app.route('/math/add')
def add():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return f"Risultato: {a + b}"
    except:
        return "Errore: parametri non validi", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
