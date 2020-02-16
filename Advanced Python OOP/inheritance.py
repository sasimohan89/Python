class User():
    def sign_in(self):
        print('Logged in')

    def attack(self):
        print('Do nothing')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'Attacking with a power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Left with arrows: {self.num_arrows}')

wizard1 = Wizard('Tanker', 100)
archer1 = Archer('Robin', 50)
# wizard1.attack()
# archer1.attack()
# print(isinstance(wizard1, Wizard))
# print(isinstance(archer1, User))
# print(isinstance(archer1, object))

# Polymorphism
def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()
