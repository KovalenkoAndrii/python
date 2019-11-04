from ZODB import FileStorage, DB
from patient import Patient
from datetime import date
import transaction

storage = FileStorage.FileStorage('mydatabase.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

zero = Patient('Surname', 'Name', date(2019, 11, 4), 'Street', 170, 80)
first = Patient('Surname1', 'Name1', date(2019, 11, 4), 'Street1', 171, 81)
root['patients'] = [zero, first]
totalWeight = 0
tallestPatient = root['patients'][0]
for dbPatient in root['patients']:
    totalWeight = totalWeight + dbPatient.weight
    if(tallestPatient.height < dbPatient.height):
        tallestPatient = dbPatient
       
print(tallestPatient)
print(totalWeight)
transaction.commit()
connection.close()
