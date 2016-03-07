file = 'mbox-short.txt'

try:
    open_file = open(file, 'r')
except:
    print('Could not open file:', file)
    quit()

c = 0

for s in open_file:
    s.strip()
    if s.startswith('From '):
        c += 1
        line = s.split()
        email = line[1]
        print(email)

print("There were", c, "lines in the file with From as the first word")
# python27
# print("There were % s lines in the file with From as the first word") % c
