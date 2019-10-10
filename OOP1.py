import random
import math
class Vector():
    def __init__(self, n):
        self.m_length = n
        self.arr = []
        for i in range(n):
            self.arr.append(random.randint(-10, 10))
    def ex_211(self):
        a = 0
        b = 0
        for i in self.arr:
            if i > 0:
                a = a + i
                b = b + 1
        return a / b
p1 = Vector(10)
print(p1.ex_211())
#############
class Vector():
    def __init__(self, n):
        self.m_length = n
        self.arr = []
        for i in range(n):
            self.arr.append(random.randint(-7, 7))
    def ex_214(self):
        a = 0
        b = 0
        for i in self.arr:
            if i < 0:
                a = a + i
                b = b + 1
        return a / b
p1 = Vector(13)
print(p1.ex_214())
class Vector():
    def __init__(self, n):
        self.m_length = n
        self.arr = []
        for i in range(n):
            self.arr.append(random.randint(1, 10))
    def ex_216(self):
        c = 1
        for i in range(len(self.arr)):
            if i % 2 == 0:
                c = c * self.arr[i]
        return c
p1 = Vector(5)
print(p1.ex_216())
###########
class Vector():
    def __init__(self, n):
        self.m_length = n
        self.arr = []
        for i in range(n):
            self.arr.append(random.randint(-20, 20))
    def ex_220(self):
        a = 0
        b = 0
        for i in self.arr:
            if i > 0:
                a = a + 1
            if i < 0:
                b = b + 1
        return ("positive =", a, "negative =", b)
p1 = Vector(10)
print(p1.ex_220())
#############
class Vector():
    def __init__(self, n):
        self.m_length = n
        self.arr = []
        for i in range(n):
            self.arr.append(random.randint(-10, 10))
    def ex_218(self):
        sum = 0
        for i in range(len(self.arr)):
            if i % 2 == 1:
                sum = sum + math.fabs(self.arr[i])
        return sum
p1 = Vector(10)
print(p1.ex_218())
############
class Vector():
    def __init__(self, n):
        self.m_length = n
        self.arr = []
        for i in range(n):
            self.arr.append(random.randint(0, 10))
    def ex_223(self, a, b):
        self.a = a
        self.b = b
        c = 0
        for i in self.arr:
            if i > self.a and self.b > i:
                c = c + 1
        return c
p1 = Vector(10)
print(p1.ex_223(4, 9))
##############
class Vector():
    def __init__(self, n):
        self.m_length = n
        self.arr = []
        for i in range(n):
            self.arr.append(random.randint(-10, 10))
    def ex_225(self, t):
        self.t = t
        product = 1
        for i in self.arr:
            if math.fabs(i) < t:
                product = product * i
        return product
p1 = Vector(7)
print(p1.ex_225(8))
##############
class Vector():
    def __init__(self, n):
        self.m_length = n
        self.arr = []
        for i in range(n):
            self.arr.append(random.randint(-100, 100))
    def ex_227(self, k):
        self.k = k
        sum = 0
        quantity = 0
        for i in range(len(self.arr)):
            if i % k == 0:
                sum = sum + self.arr[i]
                quantity = quantity + 1
        return sum / quantity
p1 = Vector(8)
print(p1.ex_227(6))
###########
class Vector():
    def __init__(self, n):
        self.m_length = n
        self.arr = []
        for i in range(n):
            self.arr.append(random.randint(-20, 20))
    def ex_229(self):
        a = 1
        for i in range(len(self.arr)):
            if self.arr[i] - i > 0:
                a = a * self.arr[i]
        return a
p1 = Vector(10)
print(p1.ex_229())
###############
class Vector():
    def __init__(self, n):
        self.m_length = n
        self.arr = []
        for i in range(n):
            self.arr.append(random.randint(-10, 10))
    def ex_230(self, k):
        self.k = k
        a = 0
        b = 0
        for i in self.arr:
            if int(i) % k == 0:
                b = b + i**2
                a = math.sqrt(b)
        return a
p1 = Vector(7)
print(p1.ex_230(7))
###############
class Building:
    def __init__(self, floor, entrance, apartment):
        self.floor = floor
        self.entrance = entrance
        self.apartment = apartment
    def func(self):
        print("floor = ", self.floor, ",", "entrance = ", self.entrance, ",", "apartment = ", self.apartment)
    def func1(self):
        return "number of apartments =", self.floor * self.entrance * self.apartment
p1 = Building(9, 4, 3)
p1.func()
print(p1.func1())
####################
class Student():
    def __init__(self, name, last_name, age, rating_1, rating_2, rating_3):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.rating_1 = rating_1
        self.rating_2 = rating_2
        self.rating_3 = rating_3
    def func(self):
        print("name =", self.name, "," "last name =", self.last_name, "," "age =", self.age, "," "rating1 =", self.rating_1,
              "," "rating2 = ", self.rating_2, "rating3 =" ",", self.rating_3)
    def func1(self):
        return "average rating =", (self.rating_1 + self.rating_2 + self.rating_3) / 3
p1 = Student("Miqayel", "Avetisyan", "20", 8 , 9, 10)
p1.func()
print(p1.func1())
##############
class Building():
    def __init__(self, floor, entrance, apartment):
        self.floor = floor
        self.entrance = entrance
        self.apartment = apartment
    def func(self):
        print("floor = ", self.floor, ",", "entrance = ", self.entrance, ",", "apartment = ", self.apartment)
    def func1(self):
        return "number of apartments =", self.floor * self.entrance * self.apartment
p1 = Building(9, 4, 3)
p1.func()
print(p1.func1())
















