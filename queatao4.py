import os
os.system("clear||cls")

#Uma fruteira está vendendo frutas com a seguinte tabela de preços: 
#Se o cliente comprar a partir de 10 Kg em frutas ou o valor total da compra ultrapassar R$ 15,00,
#receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg)
#de morangos e a quantidade (em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.

fruta = input("Fruta: ")
peso = int(input("Quantos quilos: "))

match fruta:
    case "morango":
        if peso <= 5:
            soma = peso * 2.50
        else:
            soma = peso * 2.20
    case "maçã":
        if peso <= 5:
            calculo = peso * 1.80 
        else: 
            calculo = peso * 1.50
