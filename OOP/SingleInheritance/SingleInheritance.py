class Person:

    name = ''
    age = 0

    def __init__(self, name='', age=0):
        self.name = name
        self.age = age


class Student(Person):

    student_id = ''
    student_class = ''

    def __init__(self, name='', age=0, student_id='', student_class=''):
        super().__init__(name, age)
        self.student_id = student_id
        self.student_class = student_class

    def student_details(self):
        print('Studnet Name: ', self.name)
        print('Student Age: ', self.age)
        print('Student Id: ', self.student_id)
        print('Student Class: ', self.student_class)


student_obj = Student('Mansoor', 24, '1', '10')
student_obj.student_details()
