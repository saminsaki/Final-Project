import mysql.connector

class DatabaseManager:
    def init(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def fetch_data(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

class Student:
    def init(self, student_id, name, email, class_id):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.class_id = class_id

class Teacher:
    def init(self, teacher_id, name, email):
        self.teacher_id = teacher_id
        self.name = name
        self.email = email

class Class:
    def init(self, class_id, class_name):
        self.class_id = class_id
        self.class_name = class_name

class Course:
    def init(self, course_id, course_name, teacher, students):
        self.course_id = course_id
        self.course_name = course_name
        self.teacher = teacher
        self.students = students

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)

    def edit_teacher(self, new_teacher):
        self.teacher = new_teacher

    @staticmethod
    def generate_report(courses):
        report = {}
        for course in courses:
            report[course.course_name] = len(course.students)
        return report

# Example usage
db_manager = DatabaseManager('localhost', 'root', 'password', 'school_db')
student1 = Student(1, 'Alice', 'alice@example.com', 1)
teacher1 = Teacher(1, 'Bob', 'bob@example.com')
class1 = Class(1, 'Math')
course1 = Course(1, 'Algebra', teacher1, [student1])

# Inserting data into the database
db_manager.execute_query(f"INSERT INTO students VALUES ({student1.student_id}, '{student1.name}', '{student1.email}', {student1.class_id})")
db_manager.execute_query(f"INSERT INTO teachers VALUES ({teacher1.teacher_id}, '{teacher1.name}', '{teacher1.email}')")
db_manager.execute_query(f"INSERT INTO classes VALUES ({class1.class_id}, '{class1.class_name}')")
db_manager.execute_query(f"INSERT INTO courses VALUES ({course1.course_id}, '{course1.course_name}', {teacher1.teacher_id})")

# Adding a new student to the course
student2 = Student(2, 'Bob', 'bob@example.com', 1)
course1.add_student(student2)
db_manager.execute_query(f"INSERT INTO students VALUES ({student2.student_id}, '{student2.name}', '{student2.email}', {student2.class_id})")

# Removing a student from the course
course1.remove_student(2)
db_manager.execute_query(f"DELETE FROM students WHERE student_id=2")

# Editing the teacher of the course
new_teacher = Teacher(2, 'Charlie', 'charlie@example.com')
course1.edit_teacher(new_teacher)
db_manager.execute_query(f"UPDATE courses SET teacher_id={new_teacher.teacher_id} WHERE course_id={course1.course_id}")

# Generating a report
courses_data = db_manager.fetch_data("SELECT * FROM courses")
courses = []
for course_data in courses_data:
    course_id, course_name, teacher_id = course_data
    teacher_data = db_manager.fetch_data(f"SELECT * FROM teachers WHERE teacher_id={teacher_id}")[0]
    teacher = Teacher(teacher_data[0], teacher_data[1], teacher_data[2])
    students_data = db_manager.fetch_data(f"SELECT * FROM students WHERE class_id={course_id}")
    students = [Student(student_data[0], student_data[1], student_data[2], student_data[3]) for student_data in students_data]
    courses.append(Course(course_id, course_name, teacher, students))

report = Course.generate_report(courses)

# Closing the database connection
db_manager.close_connection()

print(report)
