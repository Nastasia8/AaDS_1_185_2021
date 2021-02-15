class Person:
    def __init__(self, name, secondname, place, year):
        self.__name=name
        self.__secondname=secondname
        self.__place=place
        self.__year=year
    def Show(self):
        print(self.__name, self.__secondname, self.__place, self.__year,"года рождения")
    def GetAge():
        age=23
        return age
class Student(Person):
    def Details(self,course):
        print( "учится на ", course,"курсе")
class Teacher(Person):
    def Details1(self, subject):
        print("преподает",subject)
person1=Student("Иван","Иванов","Россия",1997,)
person1.Show()
person1.Details(4)
person2=Teacher("Петр","Сергеев","Россия", 1985)
person2.Show()
person2.Details1("математику")
del person1
del person2