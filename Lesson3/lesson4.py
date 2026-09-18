class GrandParent:
    height = 180
    satiety = 100
    age = 60

class Parent(GrandParent):
    age = 40

class Child(Parent):
    height = 50
    age = 13
    def __init__(self):
        print("Height = ", self.height)
        print("Age = ", self.age)
        print("Sateity = ", self.satiety)

child1 = Child()