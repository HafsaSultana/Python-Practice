class Cat:
    def __init__(self, color: object, action: object) -> object:
        self.color = color
        self.action = action

    def view(self):
        print(self.color, 'cat is ', self.action)

    def compare(self, ct):  # instance method
        if self.action == ct.action:
            print("Both cat are", self.action)
        else:
            print("They are different")


c1 = Cat("Red", "Sleeping")
c2 = Cat("White", "Sleeping")

c1.view()
c2.view()
c1.compare(c2)