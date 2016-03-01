loop = True
small = None
big = 0

def checkint(x):
    try:
        x = int(x)
        return x
    except:
        x = 'err'
        return x

while loop == True:

    number = input('Enter a number: ')

    if number == 'done':
        break
    else:
        number = checkint(number)

    if number == 'err':
        print('Invalid input')
        continue
    else:
        if number > big:
            big = number

        if small == None:
            small = number
        else:
            if number < small:
                small = number

print('Maximum is', big)
print('Minimum is', small)



