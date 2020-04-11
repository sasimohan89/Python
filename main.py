import re

pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
string = 'b@b.com'

# x = re.search('string', string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# print(x.span())
# print(x.group())
a = pattern.search(string)
print(a)