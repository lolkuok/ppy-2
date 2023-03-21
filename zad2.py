a = input("Liczba jedna")
b = input("liczba druga")
c = input("+ - * ** / // %")
if c == '+':
    print(f"{a} + {b} = " + str(int(a) + int(b)))
elif c == '-':
    print(f"{a} - {b} = " + str(int(a) - int(b)))
elif c == '*':
    print(f"{a} * {b} = " + str(int(a) * int(b)))
elif c == '/' and b != 0:
    print(f"{a} / {b} = " + str(int(a) / int(b)))
elif c == '//' and b != 0:
    print(f"{a} // {b} = " + str(int(a) // int(b)))
elif c == '**':
    print(f"{a} ** {b} = " + str(int(a) ** int(b)))
elif c == '%' and b != 0:
    print(f"{a} % {b} = " + str(int(a) % int(b)))
else:
    print("Nie obliczymy tego :(")

