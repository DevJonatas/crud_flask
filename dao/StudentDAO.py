from models import Student

SQL_CREATE = 'INSERT INTO student(ra, cpf, first_name, last_name, phone, date_create, date_update) VALUES (%s, %s, %s, %s, %s, now(), now())'
SQL_RETRIEVE = 'SELECT id, ra, cpf, first_name, last_name, phone, date_create, date_update FROM student ORDER BY date_update DESC'
SQL_RETRIEVE_RA = 'SELECT id, ra, cpf, first_name, last_name, phone, date_create, date_update FROM student WHERE ra = %s'
SQL_UPDATE = 'UPDATE student SET first_name=%s, last_name=%s, phone=%s, date_update=%s WHERE id=%s'
SQL_DELETE = 'DELETE FROM student WHERE id = %s'

class StudentDAO:
    def __init__(self, db):
        self.__db = db

    def save_student(self, student):
        cursor = self.__db.connection.cursor()

        if student.id:
            cursor.execute(SQL_UPDATE,(student.first_name, student.last_name, student.phone, student.date_update,student.id))
        else:
            cursor.execute(SQL_CREATE, (student.ra,student.cpf,student.first_name, student.last_name, student.phone))
        self.__db.connection.commit()
        return student

    def list_student(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_RETRIEVE)

        students = translate_student(cursor.fetchall())

        return students

    def find_student_ra(self,ra):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_RETRIEVE_RA,(ra,))
        tupla = cursor.fetchone()
        student = Student.Student(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7])

        return student

    def delete_student(self,id):
        self.__db.connection.cursor().execute(SQL_DELETE,(id,))
        self.__db.connection.commit()


def translate_student(students):
    def crete_student_with_tuple(tupla):
        return Student.Student(tupla[0],tupla[1],tupla[2],tupla[3],tupla[4],tupla[5],tupla[6],tupla[7])
    return list(map(crete_student_with_tuple, students))