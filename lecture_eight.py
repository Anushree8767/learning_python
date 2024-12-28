#OOPS
# class Student:

#     college_name = "DACN"
     
#      #default constructor
#     # def __init__(self):
#     #     pass


#     #parameterized condtructors
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        

#     def welcome(self):
#         print("welcome student", self.name)

#     def get_marks(self):
#        return self.marks
    
# s1 = Student("joy", 89)
# s1.welcome()
# print(s1.get_marks())
# print(s1.name, s1.marks)

# s2 = Student("bro", 96)
# print(s2.name, s2.marks)

# print(Student.college_name) 

#PQ-1
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod
#     def hello():
#         print("hello")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg score is:", sum/3)

# s1 = Student("tony montana", [88, 93, 92])
# s1.get_avg()
# s1.hello()

 #attributes
# class Car():
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = false

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started..")

# car1 = Car()
# car1.start()

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#     #debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print("rs.", amount, "was debited")
#         print("total balance =", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("rs.", amount, "was credited")
#         print("total balance =", self.get_balance())

#     def get_balance(self):
#         return self.balance

# acc1 = Account(10000, 12345)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(5000)

#del keyword
# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Anushree")
# print(s1.name)
# del s1.name
# print(s1.name)

# class Person:
#     __name = "anonymous"

#     def __hello(self):
#         print("hello person!")

#     def welcome(self):
#         self.__hello()

# p1 = Person()

# print(p1.welcome())

#Inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stoped")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner():
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("diesel")
# car1.start()

#multiple inheritance
# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welcome to class C"

# c1 = C()

# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

#super()
# class Car:

#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stoped")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()
        

# car1 = ToyotaCar("prius", "electric")
# print(car1.type)

#CLASS METHOD
# class Person:
#     name = "anonymous"

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name
    
# p1 = Person()
# p1.changeName("harry bro")
# print(p1.name)
# print(Person.name)

#PROPERTY decorator
# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math


#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"
        
# stu1 = Student(89, 96 , 82)
# print(stu1.percentage)

# stu1.math = 94
# print(stu1.percentage)

# print(1 + 2) #3
# print(type(1))

# print("hey" + "bro")  #concatenate

# print([1, 2, 3] + [ 4, 5, 6])  #merge

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal,  newImg)

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(6, 5)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()