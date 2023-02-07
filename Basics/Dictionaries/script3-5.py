phonebook = { "John":123, "Jack":312, "Jill":231}
for name,number in phonebook.items():
    print("Phonenumber of %s is %d" % (name, number))

del phonebook["John"] # OR -> phonebook.pop("John")
print(phonebook)