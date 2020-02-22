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
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'Left with arrows: {self.arrows}')

    def run(self):
        print('ran really fast')

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, arrows)

hb1 = HybridBorg('wiz1', 39, 100)
print(hb1.run())
print(hb1.attack())
print(hb1.check_arrows())
print(hb1.sign_in())