import sqlite3
from patient import Patient
from datetime import date

zero = Patient('Surname', 'Name', str(date(2019, 11, 4)), 'Street', 185, 80)
first = Patient('Surname1', 'Name1', str(date(2019, 11, 4)), 'Street1', 171, 81)

conn = sqlite3.connect('hospital.db')
cursor = conn.cursor()

try:
    cursor.execute("""insert into Patients values
                    (:surname, :name, :birthDate, :address,
                    :height, :weight, 1)""", {"surname": zero.surname,
                     "name": zero.name, "birthDate": zero.birth_date,
                      "address": zero.address, "height": zero.height,
                      "weight": zero.weight})
    cursor.execute("""insert into Patients values
                    (:surname, :name, :birthDate, :address,
                    :height, :weight, 2)""", {"surname": first.surname,
                     "name": first.name, "birthDate": first.birth_date,
                      "address": first.address, "height": first.height,
                      "weight": first.weight})
    cursor.execute("""SELECT *
                      FROM   Patients
                      WHERE  height=(SELECT MAX(height) FROM Patients)""")
    result = cursor.fetchall()
    print(result)
    cursor.execute("""SELECT SUM(weight) FROM Patients;""")
    result = cursor.fetchall()
    print(result)
except sqlite3.DatabaseError as err:       
    print("Error: ", err)
else:
    conn.commit()
conn.close()
