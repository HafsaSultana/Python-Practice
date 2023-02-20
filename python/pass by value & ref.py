class Cat:
    def __init__(self, color: object, action: object) -> object:
        self.color = color
        self.action = action

    def view(self, num, clr):
        num = num + 5
        clr1 = clr
        clr1[0] = 'Green'
        print("Method inside: ", num)
        print("Method inside: ", clr1)


colors = ['Black', 'Red', 'Blue', 'Orange']
c1 = Cat("Red", "Sleeping")
x = 55
c1.view(x,colors)

print("Method inside: ", x)
print("Method inside: ", colors)
