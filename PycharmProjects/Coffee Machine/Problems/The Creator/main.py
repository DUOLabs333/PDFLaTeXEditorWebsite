# create an Elf here
class Elf:
    height = 1.8
    weapon = "longbow"
    emotional_maturity = 125

    def __init__(self, name, age, catchphrase):
        self.name = name
        self.age = age
        self.catchphrase = catchphrase


legalos = Elf("legalos", 102, "boom chicka pop pop")

print(legalos.catchphrase)
