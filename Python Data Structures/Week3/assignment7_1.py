ifile = input('Enter file name: ')

try:
    ofile = open(ifile, 'r')
except:
    print('Could not find file', ifile)
    quit()

# read file into memory
rfile = ofile.read()
# strip \n and whitespace in front and end
sfile = rfile.strip()
# upper case all letters
ufile = sfile.upper()

print(ufile)