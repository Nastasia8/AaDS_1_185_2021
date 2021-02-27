class Human:
    def __init__(self, name, surname, place_of_born, year_of_born):
        self.__name = name
        self.__surname = surname
        self.__place_of_born = place_of_born
        self.__year_of_born = year_of_born

    def show(self):
        print(f"Person name is {self.__name}, surname is {self.__surname}")
        print(
            f"He was born in {self.__place_of_born} in {self.__place_of_born}")

    def GetAge(self):
        print(2021-self.__year_of_born)


class Student(Human):

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number


class Teacher(Human):
    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        self.__subject = subject


first = Human("Ivan", "Ivanov", "Ivanovo", 1999)
first.show()
first = Student
first.number = 1
