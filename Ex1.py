import datetime
import time

currentDate = time.localtime()

def check_date():
    while True:
        date_string = '22/10/2000'
        format = "%d/%m/%Y"
        dob = str(input('Enter your date of birth like dd/mm/yyyy: '))
        global y
        y = dob.split('/')
        try:
            datetime.datetime.strptime(dob, '%d/%m/%Y')
            return dob
        except:
            print("Incorrect data format, should be dd/mm/yyyy")



dob = check_date()

age = int(currentDate[0]) - int(y[2])
print('Your age is:', age)