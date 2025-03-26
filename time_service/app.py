from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/time')
def time():
    return f"Ora corrente: {datetime.datetime.now()}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
