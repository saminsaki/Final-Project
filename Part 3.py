import pandas as pd
import matplotlib.pyplot as plt

# Sample data (replace with actual data)
data = {
    'Course': ['Math', 'Science', 'History', 'English'],
    'Grades': [85, 92, 78, 88],
    'Enrollment': [50, 60, 45, 55],
    'Teacher': ['Mr. A', 'Ms. B', 'Mr. C', 'Ms. D']
}

df = pd.DataFrame(data)

def generate_grade_distribution_report():
    for course in df['Course']:
        grades = df[df['Course'] == course]['Grades']
        plt.hist(grades, bins=10, alpha=0.7, label=course)
    plt.legend()
    plt.xlabel('Grades')
    plt.ylabel('Frequency')
    plt.title('Grade Distribution Report')
    plt.show()

def display_enrollment_trends():
    df.plot(x='Course', y='Enrollment', kind='line')
    plt.xlabel('Course')
    plt.ylabel('Enrollment')
    plt.title('Enrollment Trends')
    plt.show()

def analyze_teacher_workload():
    teacher_workload = df.groupby('Teacher').agg({'Course': 'count', 'Enrollment': 'sum'})
    teacher_workload.plot(kind='bar')
    plt.xlabel('Teacher')
    plt.ylabel('Workload')
    plt.title('Teacher Workload Analysis')
    plt.show()

def summarize_student_performance():
    # Assuming student data is available in a separate dataframe
    student_data = {
        'Student': ['Alice', 'Bob', 'Charlie', 'David'],
        'Grades': [90, 85, 88, 92]
    }
    student_df = pd.DataFrame(student_data)
    
    student_df.plot(x='Student', y='Grades', kind='line', marker='o')
    plt.xlabel('Student')
    plt.ylabel('Grades')
    plt.title('Student Performance Overview')
    plt.show()

generate_grade_distribution_report()
display_enrollment_trends()
analyze_teacher_workload()
summarize_student_performance()