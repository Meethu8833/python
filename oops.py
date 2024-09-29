# class Employee:
#     id=10
#     name="Devansh"
#     def display(self):
#         print(self.id,self.name)
# d=Employee()
# d.display()

# class Employee:
#     id=10
#     name="John"
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
# emp=Employee()
# emp.display()

#______Delete the object___
# class Employee:
#     id=10
#     name="John"
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
# emp=Employee()
# del emp.id
# del emp.name
# emp.display()

#_____object_____
# class car:
#     def __init__(self,modelname,year):
#         self.modelname=modelname
#         self.year=year
#     def display(self):
#         print(self.modelname,self.year)
# c1=car("Toyota",2016)
# c1.display()

#_______creating the constructor in python________
# class Employee:
#     def __init__(self,name,id):
#         self.id=id
#         self.name=name
#     def display(self):
#         print("ID: %d\nName: %s"%(self.id,self.name))
# emp1=Employee("John",101)
# emp2=Employee("David",102)
# emp1.display()
# emp2.display()

#_______non parameterized constructor______
# class Student:
#     def __init__(self):
#         print("This is non parameterized constructor")
#     def show(self,name):
#         print("Hello",name)
# student=Student()
# student.show("John")

        
#_______parameterized constructor_______
# class Student:
#     def __init__(self,name):
#         print("This is parameterized constructor")
#         self.name=name
#     def show(self):
#         print("Hello",self.name)
# student=Student("John")
# student.show()

#_____python default constructor______
# class Student:
#     roll_num=101
#     name="Joseph"
#     def display(self):
#         print(self.roll_num,self.name)
# st=Student()
# st.display()

#____More than one constructor in single class___
# class Student:
#     def __init__(self):
#         print("The First Constructor ")
#     def __init__(self):
#         print("The second constructor")
# st=Student()

#_____built-in functions________
# class Student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
# s=Student("John",101,22)
# print(getattr(s,'name'))
# setattr(s,"age",23)
# print(getattr(s,'age'))
# print(hasattr(s,'id'))
# delattr(s,'age')
# print(s.age)

#__________inheritence____________

#___single_inheritence_____
# class Animal:
#     def speak(self):
#         print("Animal Speaking")
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
# d=Dog()
# d.bark()
# d.speak()

#____multilevel inheritence________
# class Animal:
#     def speak(self):
#         print("Animal speaking")

# class Dog(Animal):
#     def bark(self):
#         print("dog barking")

# class DogChild(Dog):
#     def eat(self):
#         print("Eating bread..")

# d=DogChild()
# d.bark()
# d.speak()
# d.eat()


#_________multiple inheritence_________
# class Calculation1:
#     def summation(self,a,b):
#         return a+b
# class Calculation2:
#     def Multiplication(self,a,b):
#         return a*b
# class Derived(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b
# d=Derived()
# print(d.summation(10,20))
# print(d.Multiplication(10,20))
# print(d.Divide(10,20))


#______Hierarchical inheritance_______
# class Parent:
#     def func1(self):
#         print("This function is in parent class")
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child 1")
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2")
# obj1=Child1()
# obj2=Child2()
# obj1.func1()
# obj1.func2()
# obj2.func1()
# obj2.func3()



#__________polymorphism____________

#_____method overriding_______
# class Animal:
#     def speak(self):
#         print("speaking")
# class Dog(Animal):
#     def speak(self):
#         print("Barking")
# d=Dog()
# d.speak()

# class Bank:
#     def getroi(self):
#         return 10
# class SBI(Bank):
#     def getroi(self):
#         return 7
# class ICICI(Bank):
#     def getroi(self):
#         return 8
# b1=Bank()
# b2=SBI()
# b3=ICICI()
# print("Bank rate of interest:",b1.getroi())
# print("Sbi rate of interest:",b2.getroi())
# print("icici rate of interest:",b3.getroi())


# class Bird:
#     def intro(self):
#         print("There are many types of birds.")
#     def flight(self):
#         print("Most of the birds can fly but some cannot")
# class sparrow(Bird):
#     def flight(self):
#         print("sparrows can fly.")
# class ostrich(Bird):
#     def flight(self):
#         print("ostriches cannot fly")
# o_b=Bird()
# o_s=sparrow()
# o_o=ostrich()
# o_b.intro()
# o_b.flight()
# o_s.intro()
# o_s.flight()
# o_o.intro()
# o_o.flight()


#_________encapsulation__________
class Base:
    def __init__(self):
        self._a=2
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class:",self._a)
        self._a=3
        print("Calling modified protected member outside class:",self._a)
obj1=Derived()
obj2=Base()
print("Accessing protected member of obj1:",obj1._a)
print("Accessing protected member of obj2:",obj2._a)