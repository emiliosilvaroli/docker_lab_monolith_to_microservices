from flask import Flask
import uuid
app = Flask(__name__)

@app.route('/uuid')
def get_uuid():
    return str(uuid.uuid4())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
