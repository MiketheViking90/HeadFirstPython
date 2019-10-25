from flask import Flask, session

app = Flask(__name__)

app.secret_key = "abc123"

@app.route('/setuser/<user>')
def setuser(user: str) -> str:
    session['user'] = user
    return 'user set to: ' + session['user']

@app.route('/getuser')
def getuser() -> str:
    return 'current user is: ' + session['user']


if __name__ == '__main__':
    app.run(debug=True)