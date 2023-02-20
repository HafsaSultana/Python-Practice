from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def Method1(self):
        print('abstractmethod 1')

    def Method2(self):
        print("hi mr")


class B(A):
    def Method1(self):
        print('Override te method 1')


c1 = B()
c1.Method1()
c1.Method2()
