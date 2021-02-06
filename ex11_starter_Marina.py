#!/usr/bin/python
from os import replace

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

a = len(Belgium)
print("-" * a)

Belgium1 = Belgium.replace(",", ":")
print(Belgium1)

Belgium2 = Belgium.split(",")
# need to use split to divide the elements within the string and convert it into a list
print(int(Belgium2[1])+int(Belgium2[3]))
