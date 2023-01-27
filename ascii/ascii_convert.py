#!/usr/bin/python3
for i in range(97, 123):
    print("{}" .format(chr(i)), end="")
    
#With the "{}" we are doing that the numbers on the var "i" are stored in {} chars.
#Example: {97} {98} ...
#With the ".format" we are changin a int to ascii char of the vay "i".
#Whith the "end=" we are printing next char followed by to the last char. 