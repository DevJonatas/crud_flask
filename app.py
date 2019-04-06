from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from dao import StudentDAO
from models import Student
import random

app = Flask(__name__)

app.config['MYSQL_HOST'] = '****'
app.config['MYSQL_USER'] = '****'
app.config['MYSQL_PASSWORD'] = '****'
app.config['MYSQL_DB'] = 'crud_flask'

mysql = MySQL(app)

student_dao = StudentDAO.StudentDAO(mysql)

@app.route('/')
def index():
    students = student_dao.list_student()
    return render_template('index.html',students=students)

@app.route('/create_student', methods=['POST',])
def create_student():
    cpf = request.form['cpf']
    ra = generate_ra()
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    phone = request.form['phone']
    student = Student.Student(None,ra, cpf, first_name, last_name, phone, None, None)

    student_dao.save_student(student)

    return redirect(url_for('index'))

def generate_ra():
    for r in range(1):
        rand = random.randint(1,10000)
    return rand

if __name__ == "__main__":
    app.run(debug=True, port=3000)