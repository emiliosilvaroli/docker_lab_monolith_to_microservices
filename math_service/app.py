from flask import Flask, request
app = Flask(__name__)

@app.route('/math/add')
def add():
    # Nessun try-except: input errati causano crash
    a = float(request.args.get('a'))  # se manca o è errato => ValueError
    b = float(request.args.get('b'))
    return f"Risultato: {a + b}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
