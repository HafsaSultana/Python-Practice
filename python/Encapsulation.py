class Student:
    school_name = 'B.N school and college, Khulna'

    def __init__(self, name, id):
        self.name = name
        self.__id = id

    def details(self):
        print('Name:', self.name, 'ID:', self.__id, 'School Name :', Student.school_name)

    def update(self, ID):
        if ID > 0:
            self.__id = ID
        else:
            print('Invalid Id, Enter id again')


s1 = Student("Bob", 22)
s2 = Student("Alic", 44)
s1.details()
s1.__id = -99

s1.update(-555)
s1.update(27)

s1.details()
