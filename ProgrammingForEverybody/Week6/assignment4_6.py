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

def computepay(h,r):
    if h < 40:
        pay = h * r
        return pay
    else:
        pay = 40 * r
        over = h - 40
        overrate = r * 1.5
        overtime = over * overrate
        pay = pay + overtime
        return pay

print(computepay(hour,rate))



