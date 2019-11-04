from datetime import date, timedelta

class Person:
    def __init__(self, name, surname, birthDate):
        self.name = name
        self.surname = surname
        self.birthDate = birthDate
        
    def CountYears(self):
        return (date.today() - self.birthDate) // timedelta(days=365.2325)

    def __str__(self) -> str:
        return f'{self.name} {self.surname} {self.birthDay}'

    
if __name__=='__main__':
    test = Person('Name','Surname',date(2017,11,4))
    print(test.CountYears())
