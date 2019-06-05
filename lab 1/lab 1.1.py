a = int(input("Введите a = "))
b = int(input("Введите b = "))
c = int(input("Введите c = "))
d = int(input("Введите d = "))
k = int(input("Введите k = "))

if b != 0 and a != 0:
    f = (((pow(a, 2) - pow(b, 3) - pow(c, 3) * pow(a, 2)) * (b - c + c * (k - d / pow(b, 3))) - (
            k / b - k / a) * c) ** 2 - 20000)
    if f > 0:
        print(f)
    else:
        print(f * (-1))
else:
    print("Del 0")