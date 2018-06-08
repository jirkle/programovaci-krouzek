#!/usr/bin/env python3

file = open("data/testfile.txt","w")
file.write("Hello World\n")
file.write("This is our new text file\n")
file.write("and this is another line.\n")
file.write("Why? Because we can.\n")
file.close()

file = open("data/testfile.txt","r")
data = file.read()
print(data)
