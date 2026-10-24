# class employee:
#     def __init__(self):
#         self.name=""
#         self.id=0
#         self.company=""
#     def details(self):
#         self.name=input("enter name:")
#         self.id=int(input("enter id:"))
#         self.company=input("enter company:")
#     def display(self):
#         print("--employee Details--")
#         print("Name of the employee:",self.name)
#         print("Company id:",self.id)
#         print("company name:",self.company)
# obj1=employee()
# obj1.details()
# obj1.display()








#......single inheritance......
# class Animal:
#     def sound(self):
#         print("Animals Make Sound....")
# class Cat(Animal):
#     def meow(self):
#         print("Cat make meow sound...")
# obj=Cat()
# obj.meow()
# obj.sound()




#practice single inheritance.....
# class Animal:
#     def eat(self):
#         print("Animals eat")
# class Dog(Animal):
#     def bark(self):
#         print("dog bark")
# obj=Dog()
# obj.eat()
# obj.bark()





#.....multiple inheritance.....
class Camera:
    def take_photo(self):
        print("Quality photos")
class Phone:
    def make_call(self):
        print("Good Photos")
class SmartPhone(Camera,Phone):
    def browse_internet(self):
        print("browse")
obj=SmartPhone()
obj.browse_internet()
obj.make_call()
obj.take_photo()


