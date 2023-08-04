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
""" class Employee:
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

 """
# method overrinding
""" class Animal:
    def run(self):
        print("Animal is running")
        
class Dog(Animal):
    def run(self):
        print("Dog is running")  
        
class Cow(Animal):
    def run(self):
        print("Cow is running") 

def animal_run(animal) :
    animal.run()         
    # Create objects
dog = Dog()
cow = Cow()
    # Call the method
animal_run(dog)
animal_run(cow) """

# polymorphism
 # method overriding occurs when a derived class,provides its implementation of a method that is already defined
 # Method Overloading allows a class to have multiple methods

class Shape:
    def calculate_area(self):
       pass
   
class Rectangle(Shape):
    def __init__(self ,length,width):
        self.length = length
        self.width =width
        
    def calculate_area(self):
        return self.length*self.width
    
class Circle(Shape):
    def __init__(self ,radius):
        self.radius =radius
        
    def calculate_area(self):
         return 3.14* self .radius* self.radius
     
# Create Shape objects
r = Rectangle(10,4)
c = Circle(6)

print( "Rectangle Area:" ,r.calculate_area())
print( "Circle Area:" , c.calculate_area())
           
    # Overloading functions
    # Function overloading means having two or more function with same name but different parameters and/orclass
class Calc:
    def add(self,x,y):
        return x +y
    def add(self, x,y,z):
        return x+y+z
 # create object 
calc =Calc()
print(calc.add(2,4,8))

# Abstraction
from abc import ABC , abstractclassmethod

class Vehicle(ABC):
    @abstractclassmethod
    def start(self):
        pass
    
    @abstractclassmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("vooom")  
        
    def stop(self):
         print("jjjj")   
         
class Truck(Vehicle):
    def start(self):
        print("start the truck")  
    def stop(self):
        print("stop the truck")
        
# Create the objects
car = Car()
truck = Truck()
# Call the methods
car.start()
car.stop()
truck.start()
truck.stop()
                 
# abstarction using calculation of area of a circle
from abc import ABC , abstractclassmethod

class Shape(ABC):
    def __init__(self, name,radius):
        self.radius = radius
    @abstractclassmethod
    def area(self):
        pass
        
class Circle(Shape):
    def __init__(self ,radius):
        self.radius =radius
        
    def calculate_area(self):
         return 3.14* self .radius* self.radius
     
class Rectangle(Shape):
    def __init__(self ,length,width):
        self.length = length
        self.width =width
        
    def calculate_area(self):
        return self.length*self.width
    
    # create the objects
    c = Circle(6)
    r = Rectangle(5,7)
    
     
     
        
    
    
           
           