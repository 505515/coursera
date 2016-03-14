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
prompt = input("Tell me something?\n")
x = type(prompt)
print(x)


x = 'Find me a word'
if 'Find' in x: print('found')
















quit()