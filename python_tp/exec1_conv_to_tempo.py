# Exercício 1:
# * Criar um programa para converter um valor em segundos em horas, minutos e segundos

# Requisitos Exercício 1:
# * O programa deve pedir os segundos ao utilizador e guardar em uma variável
# * De seguida o programa deverá calcular o total de horas, minutos e segundos e imprimir o resultado na consola

# Exemplo Exercício 1:
# - 39050 segundos é igual a 10:50:50

import time

def calcManualTeste2(option):
    segundos = option    
    segundos_rest = segundos % 86400
    horas = segundos_rest // 3600
    segundos_rest = segundos_rest % 3600
    minutos = segundos_rest // 60
    segundos_rest = segundos_rest % 60
    res2 = str(option) + " segundos é igual a " + str(horas) + ":" + str(minutos) + ":" + str(segundos_rest)
    print(res2)    
    return res2


def main():
    print ("programa para converter um valor em segundos em horas, minutos e segundos.")        
    while True:        
        try:
            option = int(input("Insira um valor em segundos (-1: para terminar): "))

            if (option == -1):
                break
            elif (option < -1):
                print("Inválido input! Tem que ser um valor positivo, pf, digite novamente.")
                continue
            else:
                tmp = time.strftime('%H:%M:%S', time.gmtime(option))
                res1 = str(option) + " segundos é igual a " + tmp
                print (res1)
                # Segundo tipo de calculo
                print ("Segundo tipo de calculo!")
                calcManualTeste2(option)                
        except ValueError:
            print("Input introduzido não é um inteiro válido!")


if __name__ == "__main__":
    main()
