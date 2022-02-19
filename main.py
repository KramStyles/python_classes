class BigObject:
    pass


class PlayerCharacter:
    techie = True

    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def run(self):
        print("Player:", self.name, "is running!")


obj1 = BigObject()
jnr = PlayerCharacter('Junior')
dan = PlayerCharacter('Daniel Edem', 24)

if __name__ == '__main__':
    dan.techie = False
    print(dan.techie)