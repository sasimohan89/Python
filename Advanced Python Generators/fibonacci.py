# # Fibonacci numbers with a generator
# def fib(number):
#     a = 0
#     b = 1
#     for i in range(number):
#         yield a
#         temp = a
#         a = b
#         b = temp + b
#     return b
#
#
# for x in fib(21):
#     print(x)

# with list
def fib2(number):
    a = 0
    b = 1
    fib_numb = []
    for i in range(number):
        fib_numb.append(a)
        temp = a
        a = b
        b = temp + b
    return fib_numb

print(fib2(1000))