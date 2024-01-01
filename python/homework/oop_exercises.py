class Student:
    def __init__(self, first_name, last_name, ID, address, age, scores):
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID
        self.address = address
        self.age = age
        self.scores = scores

student_1 = Student(input("please enter your first name: "), "Friedman", "036997989", "Geula 7 Haifa", 38, 85)

student_2 = Student("Beni", "Dror", "054567865", "Hazait 8 Tel Aviv", 42, 96)

print(student_1.first_name)
print(student_2.__dict__)

student_1_dict = (student_1.__dict__)
print(student_1_dict)







