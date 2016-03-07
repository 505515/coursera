file = 'romeo.txt'

try:
    ofile = open(file, 'r')
except:
    print('Could not find file:', file)

words = []

for w in ofile:

    wstrip = w.strip()
    sentence = wstrip.split()

    for missing in sentence:
        if missing not in words:
            words.append(missing)

words.sort()
print(words)