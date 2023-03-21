napis = "Python 2023"
a = napis
b = napis
c = napis
print(bool(a == b))
print(bool(b == c))
print(type(a), id(a))
print(type(b), id(b))
print(type(c), id(c))
c = "java 11"
print("C zmienione na java 11")
print(bool(a == b))
print(bool(b == c))
print(type(a), id(a))
print(type(b), id(b))
print(type(c), id(c))
