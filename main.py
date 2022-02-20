class BigObject:
    pass


class PlayerCharacter:
    techie = True

    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def run(self):
        print("Player:", self.name, "is running!")

    def speak(self):
        print(f"My name is {self.name} and i am {self.age} year(s) old...")

    @staticmethod
    def add(a, b):
        return a+b

    def sub(a, b):
        return a-b


class User:
    def sign_in(self):
        print('Logged in...')


class Hero(User):
    def __init__(self, name, guns) -> None:
        self.name = name
        self.guns = guns

    def shoot(self, bullets=1):
        print(self.name, "has shot", bullets, f"bullets with his {self.guns}.")


class Wizard(User):
    def __init__(self, name, powers) -> None:
        self.name = name
        self.powers = powers

    def attack(self):
        print(f"Wizard {self.name} is attacking with {self.powers}")


class Archer(Wizard):
    def shoot(self, arrows=1):
        print(f"{self.name} has shot {arrows} arrows.")


obj1 = BigObject()
jnr = PlayerCharacter('Junior')
dan = PlayerCharacter('Daniel Edem', 24)

gary = Archer('Gary Meme', 'Sharp Eyes')

if __name__ == '__main__':
    # print(PlayerCharacter.sub(3, 4))
    print(gary.shoot(4))



# Code to activate venv
# user@Users-MacBook-Air Classes % source /Users/user/Documents/Python/Classes/myvenv/bin/activate
