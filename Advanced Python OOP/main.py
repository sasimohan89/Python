class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')

    def attack(self):
        print('Do nothing')

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email) # takes from class outside
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

wizard1 = Wizard('Tanker', 100, 'a@a.com')
print(wizard1.email)

