class Student:
    def __init__(self, name, reg_no):
        self.name = name
        self.reg_no = reg_no

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Registration Number: {self.reg_no}")

student1 = Student("John Doe", "REG12345")
student1.display_info()
