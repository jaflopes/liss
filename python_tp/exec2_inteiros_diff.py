# Exercício 2:
# * Criar um programa que lê quatro valores inteiros e indica quantos são diferentes, quantos são pares e ímpares.

# Requisitos Exercício 2:
# * O programa deverá solicitar o primeiro valor e guarda-lo numa variável
# * O programa deverá solicitar o segundo valor e guarda-lo numa variável
# * O programa deverá solicitar o terceiro valor e guarda-lo numa variável
# * O programa deverá solicitar o quarto valor e guarda-lo numa variável
# * De seguida deverá validar quais são diferentes, pares e ímpares e imprimir o resultado na consola

# Exemplo Exercício 2:
# - Insira o 1º Valor: 32
# - Insira o 2º Valor: -3
# - Insira o 3º Valor: 32
# - Insira o 4º Valor: 234
# Diferentes = 3, Pares = 3, Ímpares = 1


#=====================
# input list 
input_list = [] 
  
# diferent values list 
l1 = [] 

def main():
    print ("Programa que lê quatro valores inteiros e indica quantos são diferentes, quantos são pares e ímpares.")  
    while True:              
        # an counter 
        countDiff = 0
        even_count, odd_count = 0, 0 #even=par and odd=impar
        try:
            option1 = int(input("Insira o 1º valor inteiro: "))
            input_list.append(option1)
            option2 = int(input("Insira o 2º valor inteiro: "))
            input_list.append(option2)
            option3 = int(input("Insira o 3º valor inteiro: "))
            input_list.append(option3)
            option4 = int(input("Insira o 4º valor inteiro: "))
            input_list.append(option4)


            for item in input_list: 
                # percorrer o array para saber os valores diferentes
                if item not in l1: 
                    countDiff += 1
                    l1.append(item) 
                    # print("[Debug] Diferentes: " + str(item), end = " \n") 
                
                # percorrer cada numero da lista para saber par
                if item % 2 == 0: 
                    even_count +=1
                    # print("[Debug] Par: " + str(item), end = " \n") 
                else:
                    odd_count += 1
                    # print("[Debug] Ímpar: " + str(item), end = " \n") 
            

            # printing the output 
            print("Diferentes = {0}, Pares = {1}, Ímpares = {2}".format(str(countDiff), str(even_count), str(odd_count))) 
            break
        except ValueError:
            print("Input introduzido não é um inteiro válido!")


if __name__ == "__main__":
    main()