class Book:
    def __init__(self, name: object, author: object) -> object:
        self.name = name
        self.author = author
        self.price = 0

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def details(self):  # instance method
        print('Book Name:', self.name,
              "\nAuthor:", self.author,
              "\nPrice:", self.price, 'Taka')


b1 = Book('Opekkha', "Humayon Ahmed")
b1.details()
b1.set_price(125)
# x = b1.get_price()
# print(x)
b1.details()