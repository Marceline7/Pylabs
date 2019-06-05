stroka = input()
stroka2 = stroka.split()
c = len(stroka2)
rez = []
for i in range(0, c):
    if len(stroka2[i]) > 5 and len(stroka2[i]) < 10:
        print(stroka2)
print(rez)
