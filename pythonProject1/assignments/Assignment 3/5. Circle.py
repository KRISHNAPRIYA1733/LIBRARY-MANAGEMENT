class Circle:
    def __init__(self):
        self.radius=0
    def Display(self):
        self.radius = int(input("enter circle radius:"))
    def Calculate_Area(self):
        area=3.14*self.radius**2
        print("area=", area)
    def Calculate_Perimeter(self):
        perimeter=2*3.14*self.radius
        print("Perimetr", perimeter)
obj=Circle()
obj.Display()
obj.Calculate_Area()
obj.Calculate_Perimeter()
