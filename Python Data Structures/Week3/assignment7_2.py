ifile = input('Enter file name: ')

try:
    ofile = open(ifile, 'r')
except:
    print('Could not find file', ifile)
    quit()

score = 0
count = 0

for i in ofile:
    sc = i.strip()
    if 'X-DSPAM-Confidence:' in sc:
        count = count + 1

        d = sc.find(':')
        spamstring = sc[d+1:]
        spamscore = float(spamstring)

        score = score + spamscore


avscore = score / count

print('Average spam confidence: ', avscore)