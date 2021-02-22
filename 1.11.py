class Human(object):
    def __init__(self, name, sename, place, year):
        self.name = name
        self.sename = sename
        self.place = place
        self.year = year
    def show(self):
        print(self.name, "\n", self.sename, "\n", self.place, "\n", self.year)
    def getAge(self):
        return 2021 - self.year
class Student(Human):
    def __init__(self,name, sename, place, year, curse):
        super().__init__(name, sename, place, year)
        self.curse = curse
    def show_curse(self):
        print("Curse: " + str(self.curse) )
class Teacher(Human):
    def __init__(self,name, sename, place, year, lesson):
        super().__init__(name, sename, place, year)
        self.lesson = lesson
    def Show_less(self):
        print(self.lesson)

a = Student("Евгений","Лебедев","Юрьевец",2002,1)
a.show()
a.show_curse()
print()
b = Teacher("Ольга", "Вилкина", "Омск", 1985, "Русский")
b.show()
b.Show_less()


