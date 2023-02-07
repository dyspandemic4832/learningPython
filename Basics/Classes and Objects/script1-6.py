class MyClass:
    variable = "Blah"

    def function(self):
        print("This is a message inside the class")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "LOL"

myobjectx.function()

print(myobjectx.variable)
print(myobjecty.variable)