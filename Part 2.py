import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_data(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

class Student:
    def __init__(self, student_id, name, email, class_id):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.class_id = class_id

    def add_record(self, db_manager):
        query = "INSERT INTO students VALUES (%s, %s, %s, %s)"
        params = (self.student_id, self.name, self.email, self.class_id)
        db_manager.execute_query(query, params)

    def remove_record(self, db_manager):
        query = "DELETE FROM students WHERE student_id=%s"
        db_manager.execute_query(query, (self.student_id,))

    def edit_record(self, db_manager):
        query = "UPDATE students SET name=%s, email=%s, class_id=%s WHERE student_id=%s"
        params = (self.name, self.email, self.class_id, self.student_id)
        db_manager.execute_query(query, params)

    @staticmethod
    def search_students(db_manager, search_criteria):
        query = "SELECT * FROM students WHERE name LIKE %s OR email LIKE %s"
        params = tuple(f"%{criteria}%" for criteria in search_criteria)
        return db_manager.fetch_data(query, params)

# Similarly implement classes for Teacher, Class, and Course with similar methods

# Example usage
db_manager = DatabaseManager('localhost', 'root', 'password', 'school_db')

# Adding a new student record
new_student = Student(3, 'Eve', 'eve@example.com', 1)
new_student.add_record(db_manager)

# Removing a student record
student_to_remove = Student(3, '', '', 0) # Create a student object with only student_id filled
student_to_remove.remove_record(db_manager)

# Editing a student record
student_to_edit = Student(1, 'Alice Smith', 'alice.smith@example.com', 2)
student_to_edit.edit_record(db_manager)

# Searching for students based on criteria
search_criteria = ['Alice', 'example.com']
results = Student.search_students(db_manager, search_criteria)




class Teacher:
    def __init__(self, teacher_id, name, email):
        self.teacher_id = teacher_id
        self.name = name
        self.email = email

    def add_record(self, db_manager):
        query = "INSERT INTO teachers VALUES (%s, %s, %s)"
        params = (self.teacher_id, self.name, self.email)
        db_manager.execute_query(query, params)

    def remove_record(self, db_manager):
        query = "DELETE FROM teachers WHERE teacher_id=%s"
        db_manager.execute_query(query, (self.teacher_id,))

    def edit_record(self, db_manager):
        query = "UPDATE teachers SET name=%s, email=%s WHERE teacher_id=%s"
        params = (self.name, self.email, self.teacher_id)
        db_manager.execute_query(query, params)

    @staticmethod
    def search_teachers(db_manager, search_criteria):
        query = "SELECT * FROM teachers WHERE name LIKE %s OR email LIKE %s"
        params = tuple(f"%{criteria}%" for criteria in search_criteria)
        return db_manager.fetch_data(query, params)

class Class:
    def __init__(self, class_id, class_name):
        self.class_id = class_id
        self.class_name = class_name

    def add_record(self, db_manager):
        query = "INSERT INTO classes VALUES (%s, %s)"
        params = (self.class_id, self.class_name)
        db_manager.execute_query(query, params)

    def remove_record(self, db_manager):
        query = "DELETE FROM classes WHERE class_id=%s"
        db_manager.execute_query(query, (self.class_id,))

    def edit_record(self, db_manager):
        query = "UPDATE classes SET class_name=%s WHERE class_id=%s"
        params = (self.class_name, self.class_id)
        db_manager.execute_query(query, params)

    @staticmethod
    def search_classes(db_manager, search_criteria):
        query = "SELECT * FROM classes WHERE class_name LIKE %s"
        params = (f"%{search_criteria}%",)
        return db_manager.fetch_data(query, params)

# Example usage
# Adding a new teacher record
new_teacher = Teacher(4, 'Bob Johnson', 'bob.johnson@example.com')
new_teacher.add_record(db_manager)

# Removing a teacher record
teacher_to_remove = Teacher(4, '', '') # Create a teacher object with only teacher_id filled
teacher_to_remove.remove_record(db_manager)

# Editing a teacher record
teacher_to_edit = Teacher(2, 'Jane Doe', 'jane.doe@example.com')
teacher_to_edit.edit_record(db_manager)

# Searching for teachers based on criteria
teacher_search_criteria = ['Bob', 'example.com']
results = Teacher.search_teachers(db_manager, teacher_search_criteria)

# Adding a new class record
new_class = Class(3, 'Mathematics')
new_class.add_record(db_manager)

# Removing a class record
class_to_remove = Class(3, '') # Create a class object with only class_id filled
class_to_remove.remove_record(db_manager)

# Editing a class record
class_to_edit = Class(1, 'Science')
class_to_edit.edit_record(db_manager)

# Searching for classes based on criteria
class_search_criteria = 'Math'
results = Class.search_classes(db_manager, class_search_criteria)

# Closing the database connection
db_manager.close_connection()