# from gettext import install
# # ________classes practice:____________

class student:
    def __init__(self, name, age, grade) :
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade

class course :
    def __init__(self, name, max_students) :
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students :
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)
s1 = student('tim', 19, 95)
s2 = student('bill', 19, 75)
s3 = student('jill', 19, 65)

course = course('science', 2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
print(course.get_average_grade())

______inheritance______
class pet:
     def __init__(self, name, age):
        self.name = name
        self.age = age
     def show(self):
        print(f"i am {self.name} and i am {self.age} years old")



class Cat(pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def speak(self):
        print('meow')
    def show(self):
         print(f"i am {self.name} and i am {self.age} years old and i am {self.color}")

class Dog(pet):
    def speak(self):
        print('bark')
         
p = pet('tim', 19)    
p.show()
c = Cat('bill', 34, 'red')
c.show()
d = Dog('jill', 25)
d.show()
d.speak()
c.speak()

# _______class atributes________

class Person:
    number_of_people = 0 
    
    def __init__(self, name) :
        self.name = name
        
class robot():
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def introduce_self(self):
        print('my name is ', self.name, 'my color is ',  self.color, self.weight, 'is my weight')
r1 = robot('tom', 'red', 30)
# # r1.name = "tom"
# # r1.color = "red"
# # r1.weight = 30

r2 = robot('jad', 'blue', 20)
# # r2.name = 'jad'
# # r2.color = 'blue'
# # r2.weight = 40

r1.introduce_self()
r2.introduce_self()

______________________________________________________________________________________________

class pet():
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
    
    def change_age(self, age):
        self.age = age

    def speak(self):
        print('my name is ', self.name, 'my color is ', self.color, 'and my age is ', self.age, 'years old')

Dog = pet('Tim', 'Red', 6)
Dog.change_age(9)
Dog.speak() 
cat = pet('toki', 'brown', 4)
cat.speak()
print(Dog.age)

___________________inheritance_________________

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("Hi i am ", self.name, "And i am ", self.age)

    def talk(self):
        print("Bark!")

class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color   

    def talk(self):
        print("Meow!")        

tim = Cat('Tim', 5, 'Red')
tim.talk()


