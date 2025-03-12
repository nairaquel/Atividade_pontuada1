import os
os.system("clear||cls")

#Faça um algoritmo que leia dois valores inteiros A e B 
#se os valores forem iguais deverá se somar os dois, 
#caso contrário multiplique A por B. 
#Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.

valor_a = int(input("Digite o valor A: "))
valor_b = int(input("Digite o valor B: "))

if valor_a == valor_b:
    soma = valor_b + valor_a
else: 
    soma = valor_a * valor_b

print(f"VALOR A:{valor_a}")    
print(f"VALOR B:{valor_b}")    
print(f"VALOR C:{soma}")    
  

