# Exercício 3:
# * 2520 é o número mais pequeno que pode ser dividido por todos os números de 1 até 10 sem resto de divisão. Qual é o
# número positivo mais pequeno que é uniformemente divisivel por todos os números de 1 até 20?

# Requisitos Exercício 3:
# * O programa deve correr, efetuar os calculos e imprimir o resultado na consola.


limit = 20

def greatest_common_factor(x, y):
    return y and greatest_common_factor(y, x % y) or x


def least_common_multiple(x, y):
    return x * y / greatest_common_factor(x, y)


i = 1
for item in range(1, limit):
    i = least_common_multiple(i, item)

print("Resultado: " + str(int(i)))
