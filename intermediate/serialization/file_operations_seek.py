#!/usr/bin/python

# Open a file
fo = open("foo.txt", "r+")
print("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

fo.seek(0, 0)

line = fo.readline()
print("Read Line: %s" % (line))

# Again set the pointer to the beginning
# fo.seek(0, 1)
line = fo.readline()
line3 = fo.readline()
line4 = fo.readline()

print("Read Line: %s" % (line))
print("Read Line: %s" % (line3))
print("Read Line: %s" % (line4))



# Close opend file
fo.close()
