def myfunction():
    print("Hello From my function")

def myfunction_with_args(username, greeting):
    print("Hello %s from my function, have a %s" % (username, greeting))

def sum_two_number(a, b):
    return a + b

myfunction()

username = "John"
greeting = "wonderful Day"
myfunction_with_args(username, greeting)

number = 1
other_number = 3
print(sum_two_number(number, other_number))