s = 0
for i in range(0, 6):
    n = int(input("Digite um Valor: "))
    if (n % 2 == 0):
        s = s + n
print("A soma entre os pares é {}".format(s))