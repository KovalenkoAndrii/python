from datetime import date

class Patient:
    def __init__(self, surname, name, birth_date, address, height, weight) -> None:
        self.surname = surname
        self.name = name
        self.birth_date = birth_date
        self.address = address
        self.height = height
        self.weight = weight

    def __str__(self) -> str:
        return f'{self.name} {self.surname} {self.height} {self.weight}'
