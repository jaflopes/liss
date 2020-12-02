# Exercício 4
# * Criar um programa que consiga gerar uma password aleatória, com os seguintes parâmetros:
# - Tamanho da password (entre 8 a 32 caracteres, deve pedir input ao utilizador)
# - Uppercase and Lowercase
# - Caracteres especiais
# - Digitos

# Requisitos Exercício 4:
# * O programa deve guardar a password em um ficheiro de texto
# * Deve ser utilizado os módulos random e string

import string
import random

letters = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation

# print( letters )
# print( numbers )
# print( punctuation )


def gen_pwd(length):
    # criar alfanuméricos a partir de constantes de string
    printable = f'{letters}{numbers}{punctuation}'

    # converter de string para lista e "shuffle"
    printable = list(printable)
    random.shuffle(printable)

    # gerar senha aleatória e converter em string
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    print (bcolors.OKGREEN + random_password + bcolors.ENDC)
    f = open("exec4_gen_pwd.txt", "w")
    f.write(random_password)
    f.close()


class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def main():
    print (bcolors.HEADER + "Programa para converter um valor em segundos em horas, minutos e segundos." + bcolors.ENDC)
    while True:
        try:
            length = int(input("Tamanho da password (entre 8 a 32 caracteres)(-1: para terminar): "))

            if (length == -1):
                break
            elif (length < 8 or length > 32):
                print(bcolors.WARNING + "Tamanho inválido, pf, digite novamente." + bcolors.ENDC)
                continue
            else:
                gen_pwd(length)
        except ValueError:
            print(bcolors.FAIL + "Input introduzido não é um inteiro válido!" + bcolors.ENDC)


if __name__ == "__main__":
    main()
