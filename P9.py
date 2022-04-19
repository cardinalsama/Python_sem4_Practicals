# Aim         : Consider an example of declaring the examination result.
#              Design three classes: Student, Exam, and Result. The Student class has data
#              members such as those representing rollNumber, Name, etc. Create the class Exam
#              by inheriting Student class. The Exam class adds fields representing the marks
#              scored in six subjects. Derive Result from the Exam class, and it has its own
#              fields such as total_marks. Write an interactive program to model this relationship.
# ROLL No :20CS066

class Student:
    def __init__(self, rollNo, name):
        self.rollNo = rollNo
        self.name = name

    def display(self):  # representing rollNumber, Name
        print(f'Student Roll No: {self.rollNo}')
        print(f'Student Name: {self.name}')


class Exam(Student):
    def __init__(self, rollNo, name, subject):  # take the marks scored in six subjects
        super().__init__(rollNo, name)
        self.subject = subject

    def display(self):  # representing the marks scored in six subjects
        super().display()
        for i in range(len(self.subject)):
            print(f'Subject {i} Marks: {self.subject[i]}')


class Result(Exam):
    total_marks = 0

    def __init__(self, rollNo, name, subject):  # sum marks
        super().__init__(rollNo, name, subject)
        self.total_marks = sum(subject)

    def display(self):  # representing total mark
        super().display()
        print(f'Total Marks: {self.total_marks}')


if __name__ == '__main__':
    student = Student(101, 'Renish')
    student.display()
    print()

    exam = Exam(102, 'Priya', [81, 33, 45, 47, 55, 70])
    exam.display()
    print()

    result = Result(103, 'Panth', [40, 50, 60, 79, 56, 45])
    result.display()
    print()
