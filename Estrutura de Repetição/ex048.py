s = 0
for i in range(1, 500):
    if i % 2 != 0:
        if (i % 3 == 0):
            s = s + i
print("A soma dos números impares multiplos de 3 é: {}".format(s))