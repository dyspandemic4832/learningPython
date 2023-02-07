class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f" %(self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car2 = Vehicle()

car1.name = "Fer"
car1.kind = "Convertible"
car1.color = "red"
car1.value = float(60000)

car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = float(10000)

print(car1.description())
print(car2.description())