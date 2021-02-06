#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print(Belgium)

# length of string
x=(len(Belgium))

# Part A
print("-"*x)

# Part B
x = Belgium.replace(",",":")
print(x)

# Part C
a = Belgium.split(",")
print((int(a[1]))+(int(a[3])))