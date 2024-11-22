# Teste de 2 em 2
for c in range(0, 7, 2):
    print(c)
print("FIM!")

# Teste de Decrescente
for c in range(6, 0, -1):
    print(c)
print("FIM!")

# Teste com número lido
n = int(input("Digite um Número: "))
for c in range(0, n+1):
    print(c)
print("FIM!")

# Teste com número lido e também inicio e fim com número lido
i = int(input("Digite o Início: "))
f = int(input("Digite o Fim: "))
p = int(input("Passo: "))
for c in range(i, f+1, p):
    print(c)
print("FIM!")

# Teste lendo vários números e os apresentando
for c in range(0, 3):
    n = int(input("Digite um Valor: "))
for c in range(0, 3):
    print(n)
print("FIM!")

# Somando Valores
s = 0
for c in range(0, 3):
    n = int(input("Digite um Valor: "))
    s = s + n
print("A somatória dos valores é {}".format(s))