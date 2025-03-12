import os
os.system("clear||cls")
#Em uma loja de CD´s existem apenas quatro tipos de preços que estão associados a cores.
# Assim os CD´s que ficam na loja não são marcados por preços e sim por cores. 
# Desenvolva o algoritmo que a partir da entrada da cor o software mostre o preço.
#A loja está atualmente com a seguinte tabela de preços.  


cores = input("Digite a cor: ").lower()

match cores:
    case "verde":
        print("Valor: R$10,00")
    case "azul":
        print("Valor: R$20,00")
    case "amarelo":
        print("Valor: R$30,00")
    case "vermelho":
        print("Valor: R$40,00")