from flask import flask
app = Flask(__name__)

@app.rou('/')
def home():
    return "Hello from Declerized Python App!"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)

