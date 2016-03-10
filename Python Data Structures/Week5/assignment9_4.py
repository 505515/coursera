# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail
# messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#  The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they
#  appear in the file.
#  After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most
#  prolific committer.

# output : cwen@iupui.edu 5

file = 'mbox-short.txt'

try:
    ofile = open(file, 'r')
except:
    print('Could not open file:', file)
    quit()

mbox = list()
mail = dict()

for i in ofile:
    s = i.strip()
    if s.startswith('From '):
        s = s.split()
        email = s[1]
        mbox.append(email)

for mailer in mbox:
    mail[mailer] = mail.get(mailer, 0) + 1

bigsender = None
bigcount = None


for key,value in mail.items():
    if bigcount is None or value > bigcount:
        bigsender = key
        bigcount = value

print(bigsender, bigcount)








