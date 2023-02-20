class my_calculetor:

    def product(self, num1, num2=None, num3=None):
        if num1 != None and num2 != None and num3 != None:
            print(num1 * num2 * num3)
        elif num1 != None and num2 != None:
            print(num1 * num2)
        else:
            print(num1)

    # def product(self, num1, num2, num3):
    #     print(num1 * num2 *num3)


class my_min_calculetor:

    def product(self, *num):
        pro = 1
        for i in num:
            pro = pro * i
        print(pro)


c1 = my_calculetor()
c1.product(4)
c1.product(4, 5)
c1.product(4, 5, 6)

print("Sort way using *num - ")

c2 = my_min_calculetor()
c2.product(4)
c2.product(4, 5)
c2.product(4, 5, 6,7,8,9)
