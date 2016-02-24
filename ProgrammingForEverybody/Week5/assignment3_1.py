hour = input('Hours? ')
rate = input('Rate? ')


try:
    hour = float(hour)
except:
    hour = -1

try:
    rate = float(rate)
except:
    rate = -1

if hour == -1 or rate == - 1:
    print('Please input a number')
else:
    if hour < 40:
        pay = hour * rate
        print(pay)
    else:
        pay = 40 * rate
        over = hour - 40
        overrate = rate * 1.5

        overtime = over * overrate

        pay = pay + overtime
        print(pay)

