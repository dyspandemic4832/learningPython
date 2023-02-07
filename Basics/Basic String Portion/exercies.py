s = "Hey there! what shou"
print("lenght of s = %d" % len(s))

print("The first occurrence of the letter a = %d" % s.index("a"))

print("a accurs %d times" %s.count("a"))

print("The first five characters are %s" % s[:5])
print("The next five characters are %s" % s[5:10])
print("The thirdteenth Charchter is %s" %[12])
print("The character with odd index are %s" % s[1::2])
print("The last five charchters are %s" % s[-5:])

print("String in uppercase: %s" % s.upper())
print("String in lowercase: %s" % s.lower())


if s.startswith("Hey"):
    print("String starts with 'Hey'. Good!")

if s.endswith("hou"):
    print("String ends with 'hou'. Good!")

print("Split the words of the string: %s" % s.split(" "))