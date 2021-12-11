from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def main_page():  # put application's code here
    return 'Hello, this is home page!'


@app.route('/home')
def home():
    return redirect(url_for('main_page'))

@app.route('/log-out')
def logout():
    #TODO: add some logout logic
    return redirect('/')


if __name__ == '__main__':
    app.run()
