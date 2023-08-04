class Animal:
    def __init__(self, name):
        self.name =name
    def eat(self):
        print(self.name + " is moving")
        
class Rabbit(Animal):
    def bark(self):
      print(self.name + " is barking")
                
 # create objects of the classes
Animalu = Animal("ghhh")
RabbitX = Rabbit("naks")
Animalu.eat()
RabbitX.eat()
# Multiple inheritance
class Student:
    def _init_(self,name,regno):
        self.name =name
        self.regno = regno
        
        def display_details(self):
            print(f"{self.name} am a student")
            
class Lecturer:
    def __init__(self, name):
        self.name = name
        def teach(self):
            print(f"{self.name} is teaching")


                
            
                   
            

            
                
                
                
                
                
                