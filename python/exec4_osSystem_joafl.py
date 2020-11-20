# Criar um programa em Python que permita criar, renomear, remover e listar directorias
# pag. 16
# NOTA: usar o os.system() ao invés do os.list() / dir
import os
import shutil

def criarDir():
    dir = input("Criar diretoria (nome):")
    os.mkdir(dir)
    print(bcolors.OKGREEN + "Diretoria '" + dir +
          "' criada com sucesso! Path: " + os.getcwd() + "\\" + dir + bcolors.ENDC)


def remDir():
    print("Renomear diretoria")
    dir_old = input("Nome da atual:")
    dir_new = input("Nome da nova:")
    os.rename(dir_old, dir_new)
    print(bcolors.OKGREEN + "Diretoria renomeada para '" + dir_new +
          "' com sucesso! Path: " + os.getcwd() + "\\" + dir_new + bcolors.ENDC)


def removerDir():
    # dir_rem = input("Remover diretoria (nome):")
    # os.rmdir(dir_rem)
    dir_rem = input("Remover diretoria recursivamente (nome):")
    shutil.rmtree(dir_rem)
    print(bcolors.OKGREEN + "Diretoria & Ficheiros removido(s) '" + dir_rem +
          "' com sucesso!" + bcolors.ENDC)


def listDir():
    print("Listar diretorias")
    listDirCMD = 'dir'
    os.system(listDirCMD)


# map the inputs to the function blocks
options = {1: criarDir,
           2: remDir,
           3: removerDir,
           4: listDir}


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    while True:
        try:
            print(
                "\n-Escolha as opções sobre diretorias-\n 1: criar\n 2: renomear\n 3: remover\n 4: listagem\n 5: Sair")
            option = int(input("Insira opção pretendida: "))
            print("Opção escolhida: " + str(option))
            r = range(1, 5)
            if (option in r):
                options[option]()
            elif option == 5:
                break
            else:
                print(bcolors.WARNING +
                      "Fail: Opção não é válida. Pf, Escolha de 1-5." + bcolors.ENDC)
        except ValueError:
            print(bcolors.FAIL +
                  "Fail: Value inválido. Pf, Escolha de 1-5." + bcolors.ENDC)
        # except:
        #     print(bcolors.FAIL +
        #           "Error!" + bcolors.ENDC)


if __name__ == "__main__":
    main()
