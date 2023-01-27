from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'flash message'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud_flask_app'

mysql = MySQL(app)


@app.route('/')
def Index():
    return render_template('app.html')


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        flash('Data Inserted Successfully')
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        city = request.form['city']
        pincode = request.form['pincode']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO students (name, email, phone, address, city, pincode) VALUES (%s, %s, %s, %s, %s, %s)',
                    (name, email, phone, address, city, pincode))
        mysql.connection.commit()
        return redirect(url_for('Index'))


if __name__ == '__main__':
    app.run(debug=True)
