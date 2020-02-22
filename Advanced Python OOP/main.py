# Method resolution order MRO
class A:
    def process(self):
        print('A process()')


class B:
    pass


class C(A, B):
    pass


obj = C()
obj.process()
print(C.mro())   # print MRO for class C
print(C.__mro__)    # alternative MRO print