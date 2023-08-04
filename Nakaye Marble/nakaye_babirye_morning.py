#calculate the area and circumference of the cicle
""" class Circle:   
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def circumference(self):
        return 2 * 3.14 * self.radius
    
    def __str__(self):
        return f"The area of the circle is {self.area()}"
    
    def __repr__(self):
        return f"The circumference of the circle is {self.circumference()}"
# Create object for the circle
circle1 = Circle(6)
print(circle1)
print(circle1.area())
print(circle1.circumference())
print(circle1.__str__())
print(circle1.__repr__())
 """
# Assignment1:  Show encapsulation with employee information to give an# pay increamentation (Salary with employee information to new_salary)e.g from 850000 to 1000000
class Employee:
    def __init__(self, firstname, lastname, salary):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__salary = salary
        #print("Employee created")
        
    def display_name(self):
        print(self.__firstname + self.__lastname)
    def display_salary(self):
        print(f"{self.__firstname}, your previous annual salary was $${self.__salary}")
    def display_newsalary(self):
        print(f"{self.__firstname}, your current annual salary is $${self.__salary + (10/100) * self.__salary}")
emp1 = Employee("Nakaye", "Marble", 100000)
emp1.display_name()
emp1.display_salary()
emp1.display_newsalary()
emp1.display_newsalary_Salary = emp1.self.__Salary+50000
print(emp1)


