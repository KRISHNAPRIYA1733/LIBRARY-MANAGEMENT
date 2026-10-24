class Animal:
    def sound(self):
        print("Animals make Sound!")
class Dog(Animal):
    def bark(self):
        print("Dogs barks...")
obj1=Dog()
obj1.sound()
obj1.bark()