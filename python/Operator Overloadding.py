class House:
    def __init__(self, w, d):
        self.window = w
        self.door = d

        self.new_window = None
        self.new_door = None

    def __add__(self, other):
        self.new_window = self.window + other.window
        self.new_door = self.door + other.door
        # return 'add--New house has '+str(self.new_window)+' window and '+str(self.new_door)+' door.'
        return self.new_window, self.new_door

    def view(self):
        # print('Window: ',self.window,'Door: ',self.door)
        if self.new_window == None:
            print('The house has', self.window, ' window and', self.door, 'door.')
        else:
            print('New house has', self.new_window, ' window and', self.new_door, 'door.')


h1 = House(5, 3)
h2 = House(10, 6)
h1.view()
h2.view()

print(h1 + h2)
h1.view()
h2.view()

print('---------------------------')

hw1 = House(5, 3)
hw2 = House(10, 6)
hw1.view()
hw2.view()

x, y = h1 + h2
hw3 = House(x, y)

print(hw3)
hw3.view()

print('##############---------------New Class------------------##############')

class House:
    def __init__(self, w, d):
        self.window = w
        self.door = d

    def __add__(self, other):
        new_window = self.window + other.window
        new_door = self.door + other.door

        obj = House(new_window, new_door)
        print(obj)
        return obj

    def view(self):
        print('The house has', self.window, ' window and', self.door, 'door.')


hw1 = House(5, 3)
hw2 = House(10, 6)
hw1.view()
hw2.view()

hw3 = h1 + h2
print('h1+h2----------',hw3)


hw3 = hw1 + hw2
print(hw3)
hw3.view()