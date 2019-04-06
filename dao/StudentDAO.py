from models import Student

SQL_CREATE = 'INSERT INTO student(ra, cpf, first_name, last_name, phone, date_create, date_update) VALUES (%s, %s, %s, %s, %s, now(), now())'
SQL_RETRIEVE = 'SELECT id, ra, cpf, first_name, last_name, phone, date_create, date_update FROM student'
SQL_RETRIEVE_RA = ''
SQL_UPDATE = ''
SQL_DELETE = ''

class StudentDAO:
    def __init__(self, db):
        self.__db = db

    def save_student(self, student):
        cursor = self.__db.connection.cursor()

        print(student.ra)
        print(student.cpf)

        #if student.id:
            #cursor.execute(SQL_UPDATE,(student.first_name, student.last_name, student.phone))
        #else:
        cursor.execute(SQL_CREATE, (student.ra,student.cpf,student.first_name, student.last_name, student.phone))
        self.__db.connection.commit()
        return student

    def list_student(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_RETRIEVE)

        students = translate_student(cursor.fetchall())

        return students

    def list_student_ra(self):
        pass

    def update_student(self):
        pass

    def delete_student(self):
        pass

def translate_student(students):
    def crete_student_with_tuple(tupla):
        return Student.Student(tupla[0],tupla[1],tupla[2],tupla[3],tupla[4],tupla[5],tupla[6],tupla[7])
    return list(map(crete_student_with_tuple, students))