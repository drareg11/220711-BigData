'''
OOP
-Inheritance
    -Child classes inherit methods and attributes from parent class
- Polymorphism
    - "Many Forms"
    - Ability of an object to be different classes
    -Method Overriding
        -Changing behavior of a method inherited from a parent class
    -Method Overloading 
        -Method polymorphism 
-Encapsulation
    - Having control over your attributes/ data members
    - Achieve encapsulation by making attributes private
        -*** CANT MAKE ATTRIBUTED PRIVATE IN PYTHON **
        -"Emulate" by prefixing attributes with _
    -Access attributes with control using setter/getter methods
-Abstraction
    -Handling complexity by hiding unnecessary information from the user
    -Achieved by using abstract classes
        -Class that has one or more abstract methods
            -Abstract method => unimplemented method
    -abc (Abstract Base Class) module used to create abstract classes
    

'''
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, age, color=""):
        self.name = str(name) 
        self.age = int(age)
        self.color = str(color)
       # if age < 0:
            #self.age = 0

    def setName(self, name):
        self._name = str(name)
    
    def getName(self):
        return self._name

    @abstractmethod
    def sleep(self):
        pass
   
    #def sleep(self):
       # print("***zzz***")
       

    def getOlder(self, years=1):
        self.age += years 

    @abstractmethod
    def move(self):
       # print("*", self.name, "has moved. *")
       pass

    def __str__(self):
        return "Name:" + self.name + ", Age: " + str(self.age) + ", Color: " + self.color

class Dog(Animal):
    def sleep(self):
        print("***snore***")

    def move(self):
        print("*", self.name, "ran. *")

class Cat(Animal):
    def sleep(self):
        print("***PURR***")
    def move(self):
        print("*", self.name, "walked. *" )

class Horse(Animal):
    def sleep(self):
        print("***sleep***")
    
    def move(self):
        print("*", self.name, "galloped *")

    def feed(self):
        print("** Fed", self.name, "a carrot. **")

    
