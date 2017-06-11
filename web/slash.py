from flask import Flask
app = Flask(__name__)


# NOTE: somente a URL '/flask' funciona
@app.route('/flask')
def hello_flask():
    return 'Hello Flask'


# NOTE: ambas URLs '/python' e '/python/' funcionam
@app.route('/python/')
def hello_python():
    return 'Hello Python'


if __name__ == '__main__':
    app.run()
