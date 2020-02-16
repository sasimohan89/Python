# # OOP
# print(type(None))
# print(type(True))
# print(type(5))
# print(type(5.5))
# print(type('hi'))
# print(type([]))
# print(type(()))
# print(type({}))
#
#
# class BigObject:
#     pass
#
#
# obj1 = BigObject()
#
# print(type(BigObject))
# print(type(obj1))


class PlayerCharacter:
    # cLASS oBJECT ATTRIBUTE
    membership = True
    def __init__(self, name='anonymous', age=0):
        if age>=18:
            self.name = name
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')
        return 'cool'


player1 = PlayerCharacter('Jess', 19)
player2 = PlayerCharacter('Max', 18)
player2.attack = 100
print(player1, player2)
print((player1.name))
print((player2.name))
print((player2.age))
print(player1.shout())
print(player2.attack)