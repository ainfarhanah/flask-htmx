from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'secret_key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inventory'

mysql = MySQL(app)

@app.route('/')
def index():
    title = "Login"
    return render_template('index.html', title=title)

@app.route('/register')
def register():
    title = "Register"
    return render_template('register.html', title=title)

@app.route('/contact')
def contact():
    title = "Contact"
    return render_template('contact.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)
