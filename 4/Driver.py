from Person import Person
from datetime import date, timedelta
    
class Driver(Person):
    def __init__(self, distanse, cost, label, name, surname, birthDate) -> None:
        self.distanse = distanse
        self.cost = cost
        self.label = label
        super().__init__(name, surname, birthDate)

    def __str__(self) -> str:
        return f'{self.name} {self.surname} {self.birthDate} {self.distanse} {self.cost} {self.label} {self.get_salary()}'

    def get_salary(self):
        return self.cost * self.distanse;

if __name__ == '__main__':
    test = Driver(10, 2, 'mazda', 'Name', 'Surname', date(2017, 11, 4))
    print(test.CountYears())
    print(test)
