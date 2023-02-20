class MyClass:
    def public_method(self, x):
        self.x = 9
        print("This is a public method", self.x)
        self.__private_method(77)

    def __private_method(self, y):
        self.y = 99
        print("This is a private method", self.y)


my_object = MyClass()
my_object.public_method(6)  # Output: "This is a public method"
# my_object._private_method(77)  # Output: "This is a private method"
