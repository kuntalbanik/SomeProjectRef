# Practice codes


#
# Getter & Setter
# Class example
#
#
class Student:
    def __init__(self):  # constructor
        self.__name = ""  # private variable

    def getname(self):  # getter method
        return self.__name

    def setname(self, name):  # setter method
        self.__name = name


student_obj = Student()
student_obj.setname("John")
print(student_obj.getname())


#
# Inheritance
# Another class example with 'Inheritance'
#
class GrandFather:
    def display_name_gf(self):
        print("I am Grand Father...")


class Father:
    def display_name_f(self):
        print("I am Father...")


class IamSon(GrandFather, Father):  # inherit from two classes
    def display_name_son(self):
        print("I am Son...")


inherit_obj = IamSon()
inherit_obj.display_name_f()


#
# Encapsulation
# An objects variables should not always be directly accessible
# The methods can ensure the correct values are set.
# If an incorrect value is set, the method can return an error.
#
# Private data / method
#
class EncapExample:
    __name = "John"  # private variable

    # private encapsulated method
    # unable to access ouside of the class
    def __display_name(self):
        print("Welcome to Python...")

    def __init__(self):
        print(self.__name)
        self.__display_name()


encap_obj = EncapExample()


#
# Polymorphism
# using for overloading & overriding
# polymorphism means same function name (but different signatures)
# being uses for different types
#
# example : len() function. which returns a 'list' length as well as a 'string' length
#


# overloading function
class OverLoading:
    def display_info(self, name=""):
        print("Welcome to our system " + name)


overload_obj = OverLoading()
overload_obj.display_info()


# Another example of overloading
class Area:
    def find_area(self, a=None, b=None):
        if a != None and b != None:
            print(a * b)
        elif a != None:
            print(a * a)
        else:
            print("Data not receoved...")


area_obj = Area()
area_obj.find_area()
area_obj.find_area(10)
area_obj.find_area(10, 20)


# overriding function
# It mostly used for memory reducing processes.
class IIT:
    def display_info(self):
        print("Welcome to our course for IIT...")


class IIM(IIT):
    def display_info(self):
        super().display_info()  # call parent call function using super() method
        print("Welcome to our course for IIM...")


iim_obj = IIM()
iim_obj.display_info()


def nothing(): ...
