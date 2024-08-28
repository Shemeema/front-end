class animal:
    def __init__(self,name,species,age):
        self.name=name
        self.species=species
        self.age=age
    
class dog(animal):
    def __init__(self,name,species,age,breed):
        super().__init__(name,species,age)
        self.breed=breed

    def __str__(self):
        return f"Is a {self.name} and its breed is {self.breed}"
    
d=dog("Tutu","canis",1,"German")
print(d)
        


class Animal1:
    def __init__(self, name):
        self.name = name
 
    def make_sound(self):
        pass
 
 
class Cat(Animal1):
    def make_sound(self):
        return f"{self.name} says Meow"
 
c = Cat("Bella")  
print(c.make_sound()) 


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    def __init__(self, name, age, gender, major, gpa):
        super().__init__(name, age, gender)
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return f"Name: {self.name}, Major: {self.major}, GPA: {self.gpa}"

s=Student("shemeema",24,"female","python","4.0")
print(s)




class Employee:
    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, job_title, salary, num_employees_managed):
        super().__init__(name, job_title, salary)
        self.num_employees_managed = num_employees_managed

    def __str__(self):
        return f"Name: {self.name}, Job Title: {self.job_title}, Employees Managed: {self.num_employees_managed}"


m = Manager("John", "Project Manager", 70000, 10)
print(m)



class Shape:
    def area(self):
        return 0

class Triangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def area(self):
        return 0.5 * self.width * self.height
    
    def __str__(self):
        return f"Triangle with width {self.width} and height {self.height} has an area of {self.area()}."

triangle = Triangle(10, 5)
print(triangle)