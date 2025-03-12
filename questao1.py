import os
os.system("clear||cls")

#atividade pontuada 
#data:12/03/24

#questão 1
#Faça um algoritmo que leia os valores A, B, C e 
#imprima na tela se a soma de A + B é menor que C,
#caso contrário, imprima que a A + B é maior que C. 

valor_a = int(input("Digite o primeiro valor: ")) 
valor_b = int(input("Digite o segundo valor: ")) 
valor_c = int(input("Digite o terceiro valor:"))

soma = valor_a + valor_b

if soma > valor_c:
    print(f"Valor A: {valor_a}")
    print(f"Valor B: {valor_b}")
    print(f"Valor C: {valor_c}")
    print(f"{valor_c} É maior que: {soma}")
else:
    print(f"Valor A: {valor_a}")
    print(f"Valor B: {valor_b}")
    print(f"Valor C: {valor_c}")
    print(f"{valor_c} É menor que: {soma}")

    



