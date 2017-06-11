"""
Demonstração da utilização simples dos métodos HTTP

Métodos HTTP:
    GET:    Sends data in unencrypted form to the server. Most common
            method.
    HEAD:   Same as GET, but without response body.
    POST:   Used to send HTML form data to server. Data received by
            POST method is not cached by server.
    PUT:    Replaces all current representations of the target resource
            with the uploaded content.
    DELETE: Removes all current representations of the target resource
            given by a URL.
"""

from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('success', name=user))
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
