import random
from datetime import date
from Driver import Driver

if __name__ == '__main__':
    drivers = []
    
    for _ in range(10):
        driver = Driver(random.randint(1,2000),random.randint(1, 100),
                        'mazda', 'name' + str(random.randint(1,9)), 'surname' + str(random.randint(1,9)),
                        date(random.randint(2000, 2019), random.randint(1, 12), random.randint(1, 28)))
        print(driver)
        print(driver.CountYears())
        drivers.append(driver)

    minYear = drivers[0].CountYears()
    yongDriver = drivers[0]
    for driver in drivers:
        if(minYear > driver.CountYears()):
            minYear = driver.CountYears()
            yongDriver = driver
            
    print(f'Yonger driver - {yongDriver} his count years - {minYear}')
