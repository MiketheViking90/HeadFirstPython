from flask import Flask, session

app = Flask(__name__)

app.secret_key = "abc123"

@app.route('/')
def hello() -> str:
    return 'Hello from simple webapp'

@app.route('/login')
def login() -> str:
    session['login'] = True
    return "user has logged in"

@app.route('/logout')
def logout() -> str:
    session.pop('login')
    return "user has logged out"

@app.route('/page1')
def page1() -> str:
    if is_logged_in():
        return 'page1'

@app.route('/page2')
def page2() -> str:
    if is_logged_in():
        return 'page2'

@app.route('/page3')
def page3() -> str:
    if is_logged_in():
        return 'page3'

@app.route('/status')
def status() -> str:
    if is_logged_in():
        return 'logged in'
    return 'NOT logged in'

def is_logged_in():
    return 'login' in session


if __name__ == '__main__':
    app.run(debug=True)