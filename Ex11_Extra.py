
#Exercise
#Try to fix the code to print out the correct information by changing the string.

s = "Hey there! what should this string be?"
# Length should be 20
print("Length of s = %d" % len(s))
a = s[11::]
a = a.replace("this string","this")
print("Length of a = %d" % len(a))
# %d acts as a placeholder for a number.

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))
b = s.replace("Hey there!","Hey!!")
print("The first occurrence of the letter a = %d" % b.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))
c = s.replace("Hey there!", "Ciao!")
print("a occurs %d times" % c.count("a"))
# Hey there! what should this string be?
# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[4:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5::]) # 5th-from-last to end
# last one correct?

# Convert everything to uppercase
print("String in uppercase: ", s.upper())


# Convert everything to lowercase
print("String in lowercase: ", s.lower())


# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")
if s.startswith("Hey"):
    print("String starts with 'Hey'. Good!")


# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")
if s.endswith("?"):
    print("String ends with '?'. Good!")


# Split the string into three separate strings,
# each containing only a word
# ?
print("Split the words of the string: %s" % s.split(" "))
new_lst = s.split(" ")
print(new_lst[0])
print(new_lst[1])
print(new_lst[2])