from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def main():
    return '<h3>hola</h3>'

@app.route('/login')
def user_login():
    year = date.today().year
    return render_template('login.html', year=year)

if __name__ == '__main__':
    app.run
