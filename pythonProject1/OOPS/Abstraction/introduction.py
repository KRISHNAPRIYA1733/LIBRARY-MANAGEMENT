from abc import ABC,abstractmethod
class Animal(ABC):  #parent class
    @abstractmethod
    def sound(self):  #abstract method
        pass       #do nothing
#Every class that inherits from Animal must provide its own implemetation of sound() method
class Cat(Animal):   #child class of animal,it also implements sound() method
    def sound(self):
        print("cat mewos..")
class Dog(Animal):
    def sound(self):
        print("Dog barks...")

obj=Cat()
obj.sound()

obj1=Dog()
obj1.sound()

obj2=Animal()  #Cannot create an object for animal
obj2.sound()