# OOP
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))


class BigObject:
    pass


obj1 = BigObject()

print(type(BigObject))
print(type(obj1))


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
