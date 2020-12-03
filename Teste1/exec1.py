
def calRaizQuad(num):
#: Raiz quadrada - Teste
    raiz = float(num) ** 0.5
    print(f'\nA raiz quadrada de {num} é {raiz}\n')


def main():
    while True:
        try:
            num = int(input("Escolha com um número inteiro (Numero de 0 a 20) para calcular a raiz quadrada (-1 para terminar): "))

            if (num == -1):
                break
            elif (num < 0 or num > 20):
                print("Tamanho inválido, pf, digite novamente.")
                continue
            else:
                calRaizQuad(num)
        except ValueError:
            print("Input introduzido não é um inteiro válido!")


if __name__ == "__main__":
    main()


# # 1: Raiz quadrada com o método sqrt()
# import math
# num = float(input("Entre com um número (Numero de 0 a 20):"))
# raiz = math.sqrt(num)
# print(f'\nA raiz quadrada de {num} é {raiz}\n')