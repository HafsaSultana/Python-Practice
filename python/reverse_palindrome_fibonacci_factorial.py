# -*- coding: utf-8 -*-
"""
Created on Mon May  6 01:04:45 2024

@author: Hafsa
"""
def reverse_f(s):
    s = str(s)
    return s[::-1]

print(reverse_f("Abcde"))
print(reverse_f(123456))

#--------------------------------------

def palindrom(x):
    
    s = str(x)
    if s==s[::-1]:
        print(x," is Palindrom")
    else:
        print(x," is not Palindrom")        

palindrom(12344321)
palindrom("ABBA")
palindrom("ACBU")

#--------------------------------------

def factorial(n):
    if n<=1:
        return 1
    else:
        return factorial(n-1)*n
    
print(factorial(5))

#--------------------------------------

def fibonacci(n):
    a=0
    b=1
    s=0
    for i in range(n):
        s=a+b
        print(b)
        a=b
        b=s
        
fibonacci(6)

#--------------------------------------

s = "Coding"
print(" RUN ==   ",s[:1],s[:-1],s[0:3],s[2:-1], s[::1],s[0::-1])