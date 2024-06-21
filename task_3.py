 
import mysql.connector

def connect_to_database():
    try:
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )
        cursor = conn.cursor()
        
    
        cursor.execute("CREATE DATABASE IF NOT EXISTS school")
        cursor.execute("USE school")
        
        return conn, cursor
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None, None

def create_table(cursor):
    try:
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                age INT,
                grade FLOAT
            )
        """)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def insert_student(cursor, first_name, last_name, age, grade):
    try:
        cursor.execute("""
            INSERT INTO students (first_name, last_name, age, grade)
            VALUES (%s, %s, %s, %s)
        """, (first_name, last_name, age, grade))
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def update_grade(cursor, first_name, new_grade):
    try:
        # Update the grade of a student based on first name
        cursor.execute("""
            UPDATE students
            SET grade = %s
            WHERE first_name = %s
        """, (new_grade, first_name))
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def delete_student(cursor, last_name):
    try:
        cursor.execute("""
            DELETE FROM students
            WHERE last_name = %s
        """, (last_name,))
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def fetch_all_students(cursor):
    try:

        cursor.execute("SELECT * FROM students")
        for student in cursor.fetchall():
            print(student)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def main():
    conn, cursor = connect_to_database()
    
    if conn is not None and cursor is not None:
        create_table(cursor)
        
        insert_student(cursor, "Alice", "Smith", 18, 95.5)
        insert_student(cursor, "Alice", "Doe", 22, 3.8)
        update_grade(cursor, "Alice", 97.0)
        
        fetch_all_students(cursor)
        delete_student(cursor, "Jane")
        
        fetch_all_students(cursor)
        
    
        conn.commit()
        
        
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()


