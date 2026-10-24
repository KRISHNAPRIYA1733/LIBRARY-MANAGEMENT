class Shape:
    def display(self):
        print("Drawing a shape..")
class Circle(Shape):
    def display(self):
        print("Drawing circle...")
obj=Circle()
obj.display()