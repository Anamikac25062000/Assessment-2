# 18) Python program to for student height record for a school using Class and Objects.
 

class Student:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def display_height_record(self):
        print(f"{self.name}'s height is {self.height} cm")

student1 = Student("Anamika", 160)
student2 = Student("Aamy", 159)
student3 = Student("Anu", 158)
student3 = Student("Ammu", 162)

student1.display_height_record()
student2.display_height_record()
student3.display_height_record()
