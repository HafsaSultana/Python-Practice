class parentClass:
    def __init__(self):
        print("Contractor in parent")

    def method_A(self):
        print("Method A in Parent")


class ChildClass(parentClass):
    def __init__(self):
        print("Contractor in child")

    def method_B(self):
        print("Method B in child")

c1 = ChildClass()
c1.method_A()
c1.method_B()
