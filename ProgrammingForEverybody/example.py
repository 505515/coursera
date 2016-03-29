# Hello World!

print('Hello World!')
print("Hello World!")
print("python27: print 'Hello World!'")

# variable type
h = 'Hello World!'
whatish = type(h)
print(h, whatish)

f = 13.4
whatisf = type(f)
print(f, whatisf)

f = '13,4'
whatisf = type(f)
print(f, whatisf)

x = 5
y = 2

a = x + y
b = x / y  # int result in 27, float in 3
c = x * y
d = x ** y # x^y
e = x % y
f = x // y # python3 as python27. Diviede two int gives int

print('a', a)
print('b', b)
print('c', c)
print('d', d)
print('e', e)
print('f', f)

# PEMDAS - order of calculation

x = 9
y = 5
z = 2

# Parentehses
P = (x + y)
print('P', P)
# Exponentiation
E = x ** y + z # z + y, then x^y+z
print('E', E)
# Multiplication, Division, Addidtion and Substraction
M = x * y + z # (x * y) + z
print('M', M)

# equall operators from left to right
O = x - y - z # (x - y) - z
print('O', O)

# use parentheses!

# remainer
x = 7
y = 3

a = x / y
print('a', a)

a = x % y
print(a) # 7 / 3 = 2 | 3 + 3 = 6, 1 is remainer

# if remainer equal 0, then numbers are divided by each other

# use remianer to get the last digits of a number
x = 1234
print(x % 10)
print(x % 100)
print(x % 1000)
print(x % 10000)

# Addition of text
x = 'Hello'
y = 'World!'

print(x + y)

# user input
# prompt = input("Tell me something?\n")
#x = type(prompt)
#print(x)


x = 'Find me a word'
if 'Find' in x: print('found')

# Chapter 3 - Conditional execution

x = 7
y = 5

a = x != y
print(a)
b = x > y
print(b)
c = x < y
print(c)
d = x >= y
print(d)
e = x <= y
print(e)
f = x is y
print(f)
g = x is not y
print(g)

# if same structure as for

x = 7
y = 5

if x < y:
    pass #if true, pass

if x % y == 0:
    print('x is even')
else:
    print('x is odd')

if x > y:
    pass
elif x < y:
    pass
else:
    pass

file = 'file.notxt'

try:
    f = open(file, 'r')
except:
    # catch exception
    print('could not open file:', file)

# Chapter 4 - functions

print(max('Helloworld'))
print(min('Helloworld')) # space, space is min ' '

import random

# random float between 0.0 and 1.0
x = random.random()
print(x)

# random int between 5 and 10
y = random.randint(5,10)
print(y)

# random int between 0 and 1000
z = random.randint(0,1000)
print(z)

# random from list
l = [1,2,3,4,5,6,7,8,9,10]
r = random.choice(l)
print(r)

import math
print(math)

# math functions
degrees = 45
radians = degrees / 360.0 * 2 * math.pi
s = math.sin(radians)
print(s)

txt = 'This is a txt'

def print_txt(txt):
    t = print(txt + txt)
    return(t)

p = print_txt(txt)
print(p)
print(type(print_txt))

# Chapter 5 - Iteration

# Infinite loops

x = True

while x == True:
    print(x)
    try:
        x = False
    except:
        # if x failed to set to failse, break
        break # jump out of loop
    continue # jump out of iteration

# definite loops

n = [10,20,30,40,55]
c = 0

# len
for i in n:
    c  = c + 1
    print(i)

print('Count:', c)

t = 0
# sum
for i in n:
    t = i + t

print('Total:', t)

c = len(n)
t = sum(n)

print('Count:', c, 'Total:', t)

# Chapter 6 - Strings

fruit = 'apple'
x = len(fruit)

print(fruit[x - 1]) # a
print(fruit[-1]) # a

# slice

print(fruit[:-1]) # appl
print(fruit[2:]) # ple
print(fruit[0:2]) # ap
print(fruit[:]) # apple

# strings are immutable, cant change the list of letters ie fruit[0] = 'e', fruit[:] is not 'epple', make a new string

nofruit = 'e' + fruit[1:]
print(nofruit) # epple

if 'a' in fruit: # True
    print('a is in', fruit[:])
elif 'text' in fruit:
    print('text is not in ', fruit[:])
elif 'bah' not in fruit:
    print('bah is not in ', fruit[:])

h = 'Hello World'
print(type(h))
d = dir(h)

for i in d:
    if '__' not in i:
        print('string method:', i)

# dot notifaciton -> .upper()
FRUIT = fruit.upper()
print(FRUIT)

find = fruit.find('l')
print(find)

find = fruit.find('pl')
print(find)

# find from position 1, skipping 0 where a is, returns -1, cant find 'a'
find = fruit.find('a',1)
print(find)

h = ' Hello World '
a = h.strip() # strips whitespace left and right
b = h.rstrip() # strip right
c = h.lstrip() # strip left
print(a + '\n', b + '\n', c + '\n')

h = 'Hello World'

if h.startswith('Hello'):
    print('Hello back to you')

email = 'firstname.lastname@domain.com'
atpos = email.find('@') # find at
domain = email[atpos+1:] # slice from at position + 1
print(domain)

# format operator - replace string with data stored in variable
x = 42
print('The meaning is %r' % x ) # raw
print('The meaning is %f' % x ) # float (this is %g in python2.x)
print('The meaning is %d' % x ) # decimal (int)
print('The meaning is %s' % x ) # string

y = 'txt'
z = 0.123

print('The meaning is %d or %s or %f' % (x, y, z)) # use tuple if several values

# Chapter 7 - Files

f = 'file.txt'
fopen = open(f, 'r') # if 'r' is not set file will wipe
print(fopen)

# if file is small, read the file to memory
fm = fopen.read()
print(len(fm))
print(fm[:13]) # print 13 first char in file
fopen.close()

fopen = open(f, 'r')

# search file - print v1
for i in fopen:
    if i.startswith('v1'):
       i = i.strip()
       print(i)

fopen = open(f, 'r')

# search file, skip k1
for i in fopen:
    if not i.startswith('k1'):
        continue
    else:
        i = i.strip()
        print(i)

fopen = open(f, 'r')

# if contain monkey, print it
for i in fopen:
    if i.find('monkey') == -1:
        continue

    i = i.strip()
    print(i)

# open file, read to memory, write from memory add '\nmore' and close
fopen = open(f, 'r')
fm = fopen.read()
fwrite = open(f, 'w')
fwrite.write(fm)
# fwrite.write('\nmore') # write more to file
fwrite.close()

# Chapter 8 - Lists
# list are mutable, you can replace values

l = []
print(type(l))

l = list()
print(type(l))

# list and append
l = ['1',2,'3']
l.append(4)
print(l)

# list within list
a = ['a', 'b']
b = ['aa', 'bb']
c = ['aaa', 'bbb']

x = [a,b,c]
print(x)

l = [1,2]
l[0] = 2
print(l)

if 1 not in l:
    print('1 is not in l')

# make empty list
l = []
# populate empty list with random int
for i in range(0,10):
    l.append(random.randint(1,100))
print(l)
m = l[:]

# get random int and multiply all value with 2
for i in range(len(l)):
    l[i] = l[i] * 2
print(l)

# combine two lists
print('combine')
biglist = l + m
print(biglist)

# extend the list with another list
print('extend')
e = l[:]
e.extend(m)
print(e)

# slice list
print(l[3:5])

# replace multiple values
l = ['a', 'b', 'c']
l[0:3] = ['x', 'y', 'z']
print(l)

# sort
l = []
for i in range(0,10):
    l.append(random.randint(1,100))
print(l)
l.sort() # changes the list!
print(l)

# remove from list with index 1 (no index will removfe last value)
l = ['a', 'b', 'c']
x = l.pop(1)
print(l) # return list without b
print(x) # return b

# delete from list by index 1
l = ['a', 'b', 'c']
del l[1]
print(l) # return list without b

# remove from list by value
l = ['a', 'b', 'c']
l.remove('b')
print(l) # return list without b

# bulid in functions
l = []
for i in range(0,10):
    l.append(random.randint(1,100))

print(len(l)) # lengt of list
print(max(l)) # max number
print(min(l)) # min number
print(sum(l)) # sum of all numbers
print(sum(l) / len(l)) # average

# string to list
s = 'Hello world!'
l = list(s)
print(l)

# words to list
s = 'This is an example'
l = s.split()
print(l)

# split by delimeter
s = "v1;v2;v3;v4;v5"
l = s.split(';')
print(l)

# join by delimeterd
d = ';'
s = d.join(l) # list from prev. example
print(s)

# opne file.txt and print row 2
fopen = open(f, 'r')
for i in fopen:
    if i.startswith('more'): continue
# if 'more' not in i; continue
    i = i.strip()
    w = i.split()
    print(w[1])

# Chapter 9 - Dictionaries
# simlar to list, but can use anything as index.

d = {}
print(type(d))

d = dict()
print(type(d))

d['a'] = 10
d['b'] = 20
d['c'] = 30

print(d)
print(d['a'])

# check if value exist
v = d.values()
V = 20 in v
print(type(V))
print(V)

# count letter in word, histogram
w = 'banana'
d = dict()
for c in w:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1

print(d)

d = {}
print(d)
d['a'] = 10
d['b'] = 20
d['c'] = 30

# get value
x = d.get('c', 0)
print(x) #30

# histogram with get
w = 'banana'
d = dict()
for c in w:
    d[c] = d.get(c,0) + 1

print(d)

d = {}
print(d)
d['a'] = 10
d['b'] = 20
d['c'] = 30

for key in d:
    if d[key] < 11: continue # if value is less then 11 do not print
    print(key, d[key])

import string
print(string.punctuation)

s = "This is a sentence."
#s = s.translate(None, string.punctuation) # python27
s = s.translate(s.maketrans(dict.fromkeys(string.punctuation, None)))
print(s)

# Chapter 10 - Tuples
# tuples are immutable, cant change values.

t = ()
print(type(t))

t = tuple()
print(type(t))

# compare tuples, test first value until find false value

t1 = (0,1,2)
t2 = (0,1,3)

if t1 < t2:
    print('t1 smaller then t2 (2 < 3)')
else:
    print('t1 bigger then t2')

# sort in revers order by lengt of words
s = 'There are some big and some small words in this sentence'
w = s.split()
t = list()
for word in w:
    # append list with lenght of word and word
    t.append((len(word), word))
    print(t)

t.sort(reverse=True) # sort revers
print(t)

r = list()
# get key(length of word) and value(word) that is now sorted revers in t
for key,value in t:
    # add the value into list r
    r.append(value)

print(r)

# assigne two variables at once
l = ['one', 'two']
x, y = l
print('x', x)
print('y', y)

# swap values
x, y = y, x
print('x', x)
print('y', y)

email = 'firstname.lastname@domain.com'
username, domain = email.split('@')
print(username)
print(domain)

d = {}
print(d)
d['c'] = 103
d['b'] = 234
d['a'] = 53

t = d.items()
print(t)
t = sorted(t) # use sorted instead of t.sort like in python2.7
print(t)

for key, val in d.items():
    print(val, key)


# Chapter 11 - regex

# import regex
import re

f = 'file.txt'
fopen = open(f, 'r')

# instead of .startswidth()
for i in fopen:
    i = i.strip()
    if re.search('^v2', i):
        print(i)

# re.search - True if match
# re.findall - return list with findings

x = '<firstname.lastname@domain.com>'
y = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z0-9]', x) # removes < >
print(y)

# [a-zA-Z0-9]\S*@\S*[a-zA-Z0-9], find single letter [a-zA-Z0-9], followed by zero or more no-white char. (\S*)
# Followed by an @ sign. followed by zero or more no-white char (\S*). Followed by char or numbers [a-zA-Z0-9]

# find stuff and return only matches in ()
x = 'Data with value: 100'
y = re.findall('^Data.*: ([0-9]+)', x)
print(y)

x = 'Data-with-value: 100'
y = re.findall('^Data\S*: ([0-9]+)', x)
print(y)







































quit()