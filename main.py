class BigObject:
    pass

class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("Player:", self.name, "is running!")

obj1 = BigObject()
jnr = PlayerCharacter('Junior')


if __name__ == '__main__':
    jnr.run()