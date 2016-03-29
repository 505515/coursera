import re

file = 'data.txt'

try:
    fopen = open(file, 'r')
except:
    print('Failed to open file:', file)
    quit()

s = 0

for i in fopen:
    n = re.findall('[0-9]+', i)

    for k in n:
        try:
            toint = int(k)
        except:
            print('Could not convert %r to int' % k)
            toint = 0 # set to int 0

        s = s + toint

print(s)

fopen.close()
quit()



