"""
HTTP Codes:
    400 − for Bad Request
    401 − for Unauthenticated
    403 − for Forbidden
    404 − for Not Found
    406 − for Not Acceptable
    415 − for Unsupported Media Type
    429 − Too Many Requests
"""

from flask import Flask, redirect, url_for, render_template, request, abort
# Initialize the Flask application
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        else:
            abort(401)
        return redirect(url_for('success'))
    return redirect(url_for('index'))


@app.route('/success')
def success():
    return 'logged in successfully'


if __name__ == '__main__':
    app.run(debug=True)
