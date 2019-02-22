# Write and Read text file

import os
print("Test: writeread001")
plik = open(r'C:\Users\richt\Documents\test.txt', 'w')
plik.write("Test\n")
plik.write("1234")
plik.close()

print("File contains:")
plik = open(r'C:\Users\richt\Documents\test.txt')
print(plik.read())
plik.close()
#------------------------------------------------------------------


# Check is the file exist
print("Test: check001")
if os.path.isfile(r'c:\Users\richt\Documents\test.txt'):
    print("The file name text exist")
