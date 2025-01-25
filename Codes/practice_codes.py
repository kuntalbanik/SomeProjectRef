# Practice codes


# Class example
class Student:
    def __init__(self):
        self.__name = ""

    def getname(self):
        return self.__name

    def setname(self, name):
        self.__name = name


student_obj = Student()
student_obj.setname("John")
print(student_obj.getname())
