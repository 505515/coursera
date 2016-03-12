# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each
# of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time
# using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

f = 'mbox-short.txt'

try:
    fopen = open(f, 'r')
except:
    print('Coult not open file', f)
    quit()

hourdict = dict()

for i in fopen:
    if i.startswith('From '):
        ifrom = i.split()
        time = str(ifrom[5])
        time = time.split(':')
        hour = time[0]

        hourdict[hour] = hourdict.get(hour, 0 ) + 1

hourlist = list()

for k, v in hourdict.items():
    hourlist.append( (k,v ))

hourlist.sort()

for hour, count in hourlist:
    print(hour, count)


